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
            name = cont.cleaned_data['name']
            email = cont.cleaned_data['email']
            stuClass = cont.cleaned_data['stuClass']
            newStudent = StudentDetails(id=1, name=name, stuEmail=email, stuClass=stuClass)
            newStudent.save() #same for delete: pass id and call delete() on that
    else:
        cont = Contact()
        students = StudentDetails.objects.all()
    return render(request, 'demoapp/index.html', {'contact': cont})