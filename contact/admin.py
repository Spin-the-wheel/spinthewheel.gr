from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'fname', 'surname')

    def has_add_permission(self, request):
        return False


admin.site.register(Contact, ContactAdmin)
