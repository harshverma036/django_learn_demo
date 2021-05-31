from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentDetails

def home_page(request):
    students = StudentDetails.objects.all()
    return render(request, 'demoapp/index.html', {'students': students})