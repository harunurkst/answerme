from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Write Your Question', 'class': 'form-control'}))

    class Meta:
        fields = ['text']
