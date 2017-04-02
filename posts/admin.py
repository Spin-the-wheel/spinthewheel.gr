from django.contrib import admin
from .models import Post, Video

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date', 'id', 'published')

admin.site.register(Post, PostAdmin)
admin.site.register(Video)
