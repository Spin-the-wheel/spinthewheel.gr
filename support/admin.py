from django.contrib import admin

# Register your models here.
from .models import Sponsor, Kind

admin.site.register(Sponsor)
admin.site.register(Kind)