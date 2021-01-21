from django.contrib import admin
from .models import Guest, Employee, Barbeque

# Register your models here.
admin.site.register(Guest)
admin.site.register(Employee)
admin.site.register(Barbeque)
