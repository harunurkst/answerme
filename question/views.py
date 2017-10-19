from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question
from .forms import QuestionForm
from answer.models import Answer
from answer.forms import AnswerForm


def index(request):
    # all question list for displaying on home page
    # retrieve question queryset
    questions = Question.objects.filter(is_banned=False)

    # adding paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10) # 10 question per page
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    # initialize form objects for question and answer
    question_form = QuestionForm()
    answer_form = AnswerForm()

    context = {'questions': questions,
               'question_form':question_form,
               'answer_form': answer_form}

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
        return render(request, 'question/detail.html', context)

    else:
        answer_form = AnswerForm()
        context['answer_form']=answer_form

    return render(request, 'question/detail.html', context)


def add_question(request):
    context = {}
    if request.method == 'POST':
        question_form = QuestionForm(request.POST) # form instance for post request
        context['form']= question_form

        if question_form.is_valid():
            qs_text = question_form.cleaned_data.get('text')
            # creating new question on database
            qs = Question()
            qs.text = qs_text
            if request.user.is_authenticated():
                qs.user = request.user
            qs.save()
            return redirect('question:detail', pk=qs.id)
    else:
        question_form = QuestionForm() # form instance for get request
        context['form']=question_form

    return render(request, 'question/add_question.html', {'form':question_form})
