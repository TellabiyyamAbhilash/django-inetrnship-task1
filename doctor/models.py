from django.db import models
from django.urls import reverse
# Create your models here.

class Doctor(models.Model):

    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    profilepicture  = models.ImageField(upload_to='static/images',null=True,blank=True)
    Address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('docuserdetails',kwargs={'pk':self.pk})
