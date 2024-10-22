from django import forms

class TextForm(forms.Form):
    amharic_text = forms.CharField(label='Amharic Text', widget=forms.Textarea)
