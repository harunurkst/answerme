from django import forms
from .models import Question


# class QuestionForm(forms.ModelForm):
#     qs = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Write Your Question', 'class': 'form-control'}))

#     class Meta:
#         model = Question
#         fields = ['qs']

class QuestionForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Write Your Question', 'class': 'form-control'}))

    class Meta:
        fields = ['text']
