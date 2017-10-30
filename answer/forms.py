from django import forms


class AnswerForm(forms.Form):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Answer this question', 'class': 'form-control'}))

    class Meta:
        fields = ['text']