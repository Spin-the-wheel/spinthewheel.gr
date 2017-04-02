from django.contrib import admin
from .models import Gallery, GalleryImage

# Register your models here.
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0

class GalleryAdmin(admin.ModelAdmin):
    #slug is the name of the hotel that appears in the url hyphen(/) seperated and lowercase
    prepopulated_fields = {"slug": ("title",) }
    inlines = [GalleryImageInline, ]

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage)