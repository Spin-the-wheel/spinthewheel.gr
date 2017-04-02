from django.db import models

# Create your models here.
class Gallery(models.Model):
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'gallery_image', blank=True)
    class Meta:
        verbose_name_plural = "galleries"

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    property = models.ForeignKey(Gallery, related_name='images')
    image = models.ImageField(upload_to = 'gallery_image', blank=True)
    caption = models.TextField(default='' , blank=True)

    def __str__(self):
        return self.image.url