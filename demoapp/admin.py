from django.contrib import admin
from .models import StudentDetails

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stuEmail')

admin.site.register(StudentDetails, StudentAdmin)