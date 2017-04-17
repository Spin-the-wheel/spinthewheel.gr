from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    title = models.CharField(max_length=200)
    url = models.URLField()
    body = models.TextField()
    date = models.DateField()
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'blog_image', blank=True)

class Video(models.Model):
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.link
