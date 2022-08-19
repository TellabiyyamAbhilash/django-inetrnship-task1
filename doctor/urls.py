from django.urls import path
from doctor.views import register
from doctor.views import login
from doctor.views import Filldata
from doctor.views import userdetails
from doctor.views import listdetails

urlpatterns = [

    path("register/",register, name="register"),
    path("login/",login,name='login'),
    path("fill/",Filldata.as_view(),name='docfilldetails'),
    path("details/<int:pk>",userdetails.as_view(),name='docuserdetails'),
    path("listdetails/",listdetails.as_view(),name='doclistdetails'),

]
