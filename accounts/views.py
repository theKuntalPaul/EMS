from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import StudentForm, FacultyForm
from baseapp.models import StudentFormModel, FacultyFormModel
from django.contrib.auth.models import User


class StudentFormView(View):
    form_class = StudentForm
    template_name = 'studentsignup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            department = form.cleaned_data['department']
            account = form.cleaned_data['account']

            student = StudentFormModel(account=account, username=username, department=department,
                                       password=password, first_name=first_name, last_name=last_name, email=email,)
            student.save()
            user = User.objects.create_user(
                username=username, password=password, first_name=first_name, last_name=last_name, email=email,)
            user.save()

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('studenthome')

        return render(request, self.template_name, {'form': form})


class FacultyFormView(View):
    form_class = FacultyForm
    template_name = 'facultysignup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            department = form.cleaned_data['department']
            account = form.cleaned_data['account']

            faculty = FacultyFormModel(account=account, username=username, department=department,
                                       password=password, first_name=first_name, last_name=last_name, email=email,)
            faculty.save()
            user = User.objects.create_user(
                username=username, password=password, first_name=first_name, last_name=last_name, email=email,)
            user.save()

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('facultyhome')

        return render(request, self.template_name, {'form': form})
