from django.shortcuts import render,redirect,reverse
from doctor.models import Doctor
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView,CreateView,ListView

def homepage(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docfilldetails')
    else:
        form = UserCreationForm()

    return render(request,'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('doclistdetails')
    else:
        form=AuthenticationForm()

    return render(request,'login.html',{'form':form})

class Filldata(CreateView):
    model=Doctor
    fields=('FirstName','LastName','profilepicture','Address_line1','city','state','pincode')
    template_name='doctor_fill_form.html'

class userdetails(DetailView):
    model=Doctor
    template_name='doctordetails.html'

class listdetails(ListView):
    model=Doctor
    template_name='doclistdetails.html'
