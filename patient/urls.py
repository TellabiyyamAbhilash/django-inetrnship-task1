from django.urls import path
from patient.views import register
from patient.views import login
from patient.views import Filldata
from patient.views import userdetails
from patient.views import listdetails


urlpatterns = [

    path("register/",register, name="register"),
    path("login/",login,name='login'),
    path("fill/",Filldata.as_view(),name='patfilldetails'),
    path("listdetails/",listdetails.as_view(),name='patlistdetails'),
    path("details/<int:pk>",userdetails.as_view(),name='patuserdetails'),

]
