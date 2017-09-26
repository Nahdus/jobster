

from django.contrib.auth.models import User
from django import forms
from .models import Resume

class Recruiter_register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email','password']

class Recruiter_login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','password']


class resume_submit(forms.ModelForm):
    Age = forms.CharField(max_length=2, min_length=2)
    Phone_number=forms.CharField(max_length=12, min_length=10)
    class Meta:
        model = Resume
        fields = ['Name','Age', 'Qualification','Email','Phone_number','About_Me','Skills']



