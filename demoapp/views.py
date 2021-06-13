from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import StudentDetails
from .forms import Contact

def password_validate(request):
    return HttpResponse('Password did not match')

def home_page(request):
    if request.method == 'POST':
        cont =  Contact(request.POST)
        if cont.is_valid():
            print(cont.cleaned_data['email'])
            print(cont.cleaned_data['password'])
            print(cont.cleaned_data['confirm_password'])
    else:
        cont = Contact()
        students = StudentDetails.objects.all()
    return render(request, 'demoapp/index.html', {'contact': cont})