from django import forms

class Contact(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email...' }))
    password = forms.CharField(widget=forms.PasswordInput({ 'placeholder': 'Enter Password..' }))