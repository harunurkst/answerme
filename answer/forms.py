from django import forms


class AnswerForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Answer this question', 'class': 'form-control'}))

    class Meta:
        fields = ['text']