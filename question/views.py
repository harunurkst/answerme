from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from taggit.models import Tag

from .models import Question
from .forms import QuestionForm, TagForm
from answer.models import Answer
from answer.forms import AnswerForm


def index(request, tag_slug=None):
    # all question list for displaying on home page
    # retrieve question queryset
    questions = Question.objects.filter(is_banned=False)

    # if valid tag_slug is presented
    # filter all questions with that tag
    tag = None # initialize tag variable for template context
    if tag_slug:
        # retrieve submitted tag from Tag model
        tag = get_object_or_404(Tag, slug=tag_slug)
        # retrieve all question including this tag
        questions = questions.filter(tags__in=[tag])


    # adding paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10) # 10 question per page
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    # initialize form objects for question and answer and tag
    question_form = QuestionForm()
    answer_form   = AnswerForm()
    tag_form      = TagForm()

    context = {'questions': questions,
               'question_form':question_form,
               'answer_form': answer_form,
               'tag_form':tag_form,
               'tag':tag}

    return render(request, 'question/index.html', context)


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {'question':question}

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)

        if answer_form.is_valid():
            answer_text = answer_form.cleaned_data.get('text')

            #creating new answer for this question
            new_answer = Answer()
            new_answer.text = answer_text
            if request.user.is_authenticated():
                new_answer.user = request.user
            new_answer.question = question
            new_answer.save()

            #message for successful save
            context['answer_saved']=True
            answer_form = AnswerForm()

        context['answer_form'] = answer_form
        # return render(request, 'question/detail.html', context)
        return redirect(request.META['HTTP_REFERER']) # redirect to same url (where form was submitted )

    else:
        answer_form = AnswerForm()
        context['answer_form']=answer_form


    return render(request, 'question/detail.html', context)


def add_question(request):
    context = {}
    if request.method == 'POST':
        question_form = QuestionForm(request.POST) # question form instance for post request
        tag_form = TagForm(request.POST) # tag form instance for post request
        context['question_form']= question_form

        if question_form.is_valid():
            qs_text = question_form.cleaned_data.get('text')
            # creating new question from model
            qs = Question.objects.create(text=qs_text)

            # adding tags to question if provided
            if tag_form.is_valid():
                tags = tag_form.cleaned_data.get('tag')
                # if tag field is not empty
                if tags:
                    # tag string splited into list, separeted (splited) by comma.
                    # then expend this tag list into multiple arguments of
                    # add method as he expected.
                    qs.tags.add(*tags.split(','))

            # add current user as asker if user is authenticated
            if request.user.is_authenticated():
                qs.user = request.user
                # add asker as subscriber of his question
                qs.subscribers.add(request.user)

            # save and commit question
            qs.save()
            return redirect('question:detail', pk=qs.id)
    else:
        question_form = QuestionForm() # question form instance for get request
        tag_form = TagForm() # tags form instance for get request

        # adding tag form and question form on template context
        context['question_form']=question_form
        context['tag_form']=tag_form

    return render(request, 'question/add_question.html', context)


@login_required
def subscribe_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.subscribers.add(request.user)
    return redirect(request.META['HTTP_REFERER'])  # redirect to same url (where form was submitted )


@login_required
def unsubscribe_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.subscribers.remove(request.user)
    return redirect(request.META['HTTP_REFERER'])  # redirect to same url (where form was submitted )
