from django import forms

class Contact(forms.Form):
    name = forms.CharField(error_messages={'required': 'please enter your name'})
    email = forms.CharField(widget=forms.EmailInput, error_messages={'required': 'Enter your email'})
    stuClass = forms.IntegerField(error_messages={'required': 'please enter class'})

    def clean(self):
        nameValue = self.cleaned_data['name']
        if len(nameValue) < 5 or len(nameValue) == 0:
            raise forms.ValidationError('please enter more than 4 digits.')
    # JISKO CLEAN KRNA HOGA USKO clean_<fieldName>