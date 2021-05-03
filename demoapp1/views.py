from django.shortcuts import render
from django.http import HttpResponse

def about_page(request):
    return render(request, 'demoapp1/about.html')