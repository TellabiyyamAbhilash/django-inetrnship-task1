from django.contrib import admin

# Register your models here.
from patient.models import Patient

# to show the objects in admin ui as tables
class PatientAdmin(admin.ModelAdmin):
    list_display=['id','FirstName','LastName','profilepicture','Address_line1','city','state','pincode']

# Register your models here.
admin.site.register(Patient,PatientAdmin)
