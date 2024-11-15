from django import forms
from django.core.exceptions import ValidationError

class TextForm(forms.Form):
    amharic_text = forms.CharField(widget=forms.Textarea, max_length=500)  # Limit to 500 characters
    number_of_suggestions = forms.IntegerField(min_value=1, initial=1)

    def clean_amharic_text(self):
        text = self.cleaned_data.get('amharic_text')

        # If the text length exceeds 500 characters, raise a ValidationError
        if len(text) > 500:
            raise ValidationError("The text is too long. Maximum allowed length is 500 characters.")

        return text
