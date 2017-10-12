from django.shortcuts import render
from .forms import QuestionForm
from .models import Question
from django.shortcuts import redirect


def home(request):
    form = QuestionForm
    questions = Question.objects.order_by('-date')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    if request.user.is_authenticated():
        user_name = request.user.name
    else:
        user_name = request.user

    context = {'form': form, 'questions': questions, 'user_name': user_name}
    return render(request, 'index.html', context)
