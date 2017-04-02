
from django import forms

class ContactForm(forms.Form):
    fname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your Message here..'}))