from django import forms

class Contact(forms.Form):
    name = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pwd = self.cleaned_data['password']
    #     c_pwd = self.cleaned_data['confirm_password']
    #     if pwd != c_pwd:
    #         raised forms.ValidationError('Password do not match')
    # JISKO CLEAN KRNA HOGA USKO clean_<fieldName>
    def clean_password(self):
        nameValue = self.cleaned_data['name']
        if len(nameValue) < 5:
            raise forms.ValidationError('please enter more than 4 digits.')
        return nameValue