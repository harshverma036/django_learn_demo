from django.shortcuts import render

def my_page(request):
    return render(request, 'index.html')