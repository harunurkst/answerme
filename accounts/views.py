from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from question.models import Question

from .forms import UserForm, ProfileForm


@login_required
def dashboard(request):
    asked_question_list = Question.objects.filter(user=request.user) # all question asked by current user
    subscribed_question_list = request.user.subscribed.all() # all question subscribed by current user

    context = {'user':request.user,
               'asked_question_list':asked_question_list,
               'subscribed_question_list':subscribed_question_list,
        }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            current_user = get_object_or_404(User, pk=request.user.pk)
            current_user.first_name = user_form.cleaned_data.get('first_name')
            current_user.last_name = user_form.cleaned_data.get('last_name')
            current_user.email = user_form.cleaned_data.get('email')

            current_user.profile.photo = profile_form.cleaned_data.get('photo', 'photo not added yet.')
            current_user.profile.website = profile_form.cleaned_data.get('website')
            current_user.profile.location = profile_form.cleaned_data.get('location')

            current_user.save()
            return redirect(reverse('accounts:profile'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)


    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'accounts/profile_update_form.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:login')
    return render(request, 'allauth/account/login.html')

def user_logout(request):
    logout(request)
    return redirect('question:index')

