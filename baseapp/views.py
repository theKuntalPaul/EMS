from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import StudentLoginForm, FacultyLoginForm, StudentUpdateMarksForm
from baseapp.models import Semester, StudentFormModel, StudentUpdateMarksModel


class IndexPageView(TemplateView):
    template_name = 'index.html'


def StudentHomePageView(request):
    marks = StudentUpdateMarksModel.objects.order_by('sem')
    return render(request, 'studenthome.html', {'marks': marks})


class FacultyHomePageView(ListView):
    model = StudentFormModel
    ordering = ["department"]
    template_name = 'facultyhome.html'


class StudentLoginView(View):
    form_class = StudentLoginForm
    template_name = 'studentlogin.html'

    def get(self, request):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('studenthome')
        return render(request, self.template_name, {'form': form})


class FacultyLoginView(View):
    form_class = FacultyLoginForm
    template_name = 'facultylogin.html'

    def get(self, request):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('facultyhome')
        return render(request, self.template_name, {'form': form})


def StudentDetailView(request):

    if request.method == 'POST':
        form = StudentUpdateMarksForm(request.POST)
        if form.is_valid():
            sem = form.cleaned_data['sem']
            name = form.cleaned_data['name']
            subject_1 = form.cleaned_data['subject_1']
            subject_2 = form.cleaned_data['subject_2']
            subject_3 = form.cleaned_data['subject_3']
            subject_4 = form.cleaned_data['subject_4']
            new_req = StudentUpdateMarksModel(sem=sem,
                                              name=name,
                                              subject_1=subject_1,
                                              subject_2=subject_2,
                                              subject_3=subject_3,
                                              subject_4=subject_4)
            new_req.save()
            return redirect('facultyhome')
    else:
        form = StudentUpdateMarksForm()
    return render(request, 'studentdetails.html', {'form': form})





