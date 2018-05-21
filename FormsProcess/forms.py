# -*- coding:utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)  # required为可选项
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        words = len(message.split())
        if words < 4:
            raise forms.ValidationError('not enough words.')
        return message