from django.contrib import admin
from .models import StudentFormModel, FacultyFormModel, Semester, Department, StudentUpdateMarksModel
admin.site.register(Department)
admin.site.register(StudentFormModel)
admin.site.register(FacultyFormModel)
admin.site.register(Semester)
admin.site.register(StudentUpdateMarksModel)



