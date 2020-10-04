from taskapp.models import employee
from django import forms
from django.core.exceptions import ValidationError

class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"

#def mobile_num(value):
    #if len(value)<10:
        #raise forms.ValidationError("Mobile number must be 10 digits")

def clean(self):
    mobilenumber=self.cleaned_data["emobileno"]
    if len(mobilenumber)<10:
        raise forms.ValidationError("Mobile number miust be 10 digits")
    return mobilenumber

def gmail_verification(self):
    mail=self.cleaned_data("email")
    if len(mail)<10:
        raise forms.ValidationError("plz cjeck mail")
    return mail