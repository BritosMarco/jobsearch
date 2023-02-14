from django.contrib import admin
from .models import Professional, JobAcademic, JobExperience

# Register your models here.

admin.site.register(Professional)
admin.site.register(JobAcademic)
admin.site.register(JobExperience)
