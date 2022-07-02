from django.contrib import admin
from .models import appointment,doctors, feedback
# Register your models here.
admin.site.register(appointment) 
admin.site.register(doctors)
admin.site.register(feedback)