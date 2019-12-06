from django.contrib import admin
from .models import Scholarship, Applicant, Donor, Parent, School, Tuition_Fee

# Register your models here.
admin.site.register(Scholarship)
admin.site.register(Applicant)
admin.site.register(Donor)
admin.site.register(Parent)
admin.site.register(School)
admin.site.register(Tuition_Fee)
