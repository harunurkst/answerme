from django.shortcuts import render
from .forms import QuestionForm
from .models import Question
from django.shortcuts import redirect


def home(request):
    form = QuestionForm
    questions = Question.objects.order_by('-date')
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form,
               'questions':questions
               }
    return render(request, 'index.html',context)
