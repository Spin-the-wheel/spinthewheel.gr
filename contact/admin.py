from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'fname', 'surname')

admin.site.register(Contact, ContactAdmin)
