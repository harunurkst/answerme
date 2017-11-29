from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(label='',
                           widget=forms.Textarea(attrs={'placeholder': 'Write what you want to know',
                                                         'class': 'form-control',
                                                         }))

    class Meta:
        fields = ['text']