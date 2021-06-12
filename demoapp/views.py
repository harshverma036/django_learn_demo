from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentDetails
from .forms import Contact

def home_page(request):
    form_data = None
    students = None
    if request.method == 'POST':
        cont = Contact(request.POST)
        if cont.is_valid():
            print(cont.cleaned_data['email'])
            print(cont.cleaned_data['password'])
            form_data = { 'email': cont.cleaned_data['email'], 'password': cont.cleaned_data['password'] }
        else:
            print('Invalid Data')
    else:
        cont = Contact()
        students = StudentDetails.objects.all()
    return render(request, 'demoapp/index.html', {'students': students, 'contact': cont, 'form_data': form_data})