from django.contrib import admin


# Register your models here.
from .models import Person, Role

admin.site.register(Person)
admin.site.register(Role)