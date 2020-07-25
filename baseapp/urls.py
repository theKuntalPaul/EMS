from django.urls import path
from . import views

urlpatterns = [

    path('', views.IndexPageView.as_view(), name='homepage'),
    path('student/', views.StudentLoginView.as_view(), name='student'),
    path('faculty/', views.FacultyLoginView.as_view(), name='faculty'),
    path('studenthome/', views.StudentHomePageView, name='studenthome'),
    path('facultyhome/', views.FacultyHomePageView.as_view(), name='facultyhome'),
    path('studentdet/', views.StudentDetailView, name='studentdet'),

]



