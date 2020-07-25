from django.urls import path
from . import views

urlpatterns = [
    path('studentsignup/', views.StudentFormView.as_view(), name='studentsignup'),
    path('facultysignup/', views.FacultyFormView.as_view(), name='facultysignup'),
]



