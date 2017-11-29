from django import forms

class TagForm(forms.Form):
    tag = forms.CharField(label='',
                          required=False,
                          max_length=255,
                          widget=forms.TextInput(attrs={'placeholder':'Write Comma Separated Tags. (optional)',
                                                        'class': 'form-control'})
                          )

class CategoryForm(forms.Form):
    tag = forms.CharField(label='',
                          required=False,
                          max_length=255,
                          widget=forms.TextInput(attrs={'placeholder':'Write Comma Separated Category. (optional)',
                                                        'class': 'form-control'})
                          )