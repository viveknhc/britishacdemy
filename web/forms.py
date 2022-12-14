from django import forms
from web.models import Contact, Feedback, Subscriber
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput, URLInput, Select, NumberInput, RadioSelect, FileInput, ClearableFileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off', 'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off', 'placeholder': 'Your Email'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number', 'required': 'required', 'autocomplete': 'off', 'placeholder': 'Your Phone'}),
            'subject': TextInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off', 'placeholder': 'Your Subject'}),
            'message': Textarea(attrs={'class': 'form-control', 'name': 'comments', 'rows': '5', 'data-msg-required': 'This field is required.', 'placeholder': 'Your Message'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control ', 'required': 'required', 'autocomplete': 'off', 'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off', 'placeholder': 'Your Email'}),
            'message': Textarea(attrs={'class': 'form-control', 'name': 'comments', 'rows': '4', 'placeholder': 'Your Message'}),
        }


class SubsriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'required', 'autocomplete': 'off', 'placeholder': 'Your Email'}),

        }
