from django.contrib import admin

# Register your models here.
from .models import Sponsor, Kind

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'url')

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Kind)
