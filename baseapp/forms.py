from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import StudentFormModel, FacultyFormModel, StudentUpdateMarksModel


class StudentLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'letters, digits and @/./+/-/_'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))

    class Meta:
        model = StudentFormModel
        fields = ['username', 'password']


class FacultyLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'letters, digits and @/./+/-/_'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))

    class Meta:
        model = FacultyFormModel
        fields = ['username', 'password']


class StudentUpdateMarksForm(forms.ModelForm):
    
    subject_1 = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': 'number'}))
    subject_2 = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': 'number'}))
    subject_3 = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': 'number'}))
    subject_4 = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': 'number'}))

    class Meta:
        model = StudentUpdateMarksModel
        fields = ['sem', 'name', 'subject_1', 'subject_2', 'subject_3', 'subject_4']


