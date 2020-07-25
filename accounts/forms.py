from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from baseapp.models import StudentFormModel, FacultyFormModel


class StudentForm(forms.ModelForm):
    
    acctype = [('', ''), ('Student', 'Student'), ]

    account = forms.ChoiceField(choices=acctype)
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'letters, digits and @/./+/-/_'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'lastname'}))
    
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'email address'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))

    class Meta:
        model = StudentFormModel
        fields = ['account', 'username', 'first_name', 'last_name',
                  'department', 'email', 'password']


class FacultyForm(forms.ModelForm):
    
    acctype = [('', ''), ('Faculty', 'Faculty'), ]

    account = forms.ChoiceField(choices=acctype)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'letters, digits and @/./+/-/_'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'lastname'}))
    
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'email address'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))

    class Meta:
        model = FacultyFormModel
        fields = ['account', 'username', 'first_name', 'last_name',
                  'department', 'email', 'password']

