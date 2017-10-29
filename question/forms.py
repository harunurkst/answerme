from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Write Your Question', 'class': 'form-control'}))

    class Meta:
        fields = ['text']


class TagForm(forms.Form):
    tag = forms.CharField(label='', required=False, max_length=34, widget=forms.TextInput(attrs={'placeholder':'Write Comma Separated Tags. (optional)',
                                                                                                 'class': 'form-control'}))