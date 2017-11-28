from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Write what you want to know',
                                                         'class': 'ask-input w-input',
                                                         'maxlength':'256',
                                                         'autofocus':'true',
                                                         'name':'name',
                                                         'data':'Name',
                                                         'id':'name',
                                                         }))

    class Meta:
        fields = ['text']