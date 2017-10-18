from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question
from .forms import QuestionForm
from answer.models import Answer
from answer.forms import AnswerForm


def index(request):
    # retrieve question queryset
    questions = Question.objects.filter(is_banned=False)

    #add paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10) # 10 question per page
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    #adding page object to context
    context = {'questions': questions}
    return render(request, 'question/index.html', context)

def add_question(request):
    context = {}
    if request.method == 'POST':
        form = QuestionForm(request.POST) # form instance for post request
        context['form']= form

        if form.is_valid():
            qs_text = form.cleaned_data.get('text')
            # creating new question on database
            q = Question()
            q.text = qs_text
            if request.user.is_authenticated():
                q.user = request.user
            q.save()
            return redirect('/')
    else:
        form = QuestionForm() # form instance for get request
        context['form']=form

    return render(request, 'question/add_question.html', {'form':form})


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

