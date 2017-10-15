from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import QuestionForm
from .models import Question


def index(request):
    questions = Question.objects.filter(is_banned=False)
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


class QuestionDetail(DetailView):
    model = Question
    template_name = 'question/detail.html'
