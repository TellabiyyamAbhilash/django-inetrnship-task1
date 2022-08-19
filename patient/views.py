from django.shortcuts import render,redirect
from patient.models import Patient
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,DetailView,ListView

def homepage(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patfilldetails')
    else:
        form = UserCreationForm()

    return render(request,'patregister.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('patlistdetails')
    else:
        form=AuthenticationForm()

    return render(request,'patlogin.html',{'form':form})

class Filldata(CreateView):
    model=Patient
    fields=('FirstName','LastName','profilepicture','Address_line1','city','state','pincode')
    template_name='patient_fill_form.html'

class userdetails(DetailView):
    model=Patient
    template_name='Patientdetails.html'

class listdetails(ListView):
    model=Patient
    template_name='patlistdetails.html'
