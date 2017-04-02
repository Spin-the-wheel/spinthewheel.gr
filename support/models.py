from django.db import models

# Create your models here.
class Kind(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Sponsor(models.Model):
    image = models.ImageField(upload_to = 'sponsor_image', blank=True)
    name = models.CharField(max_length=200)
    title = models.ForeignKey(Kind)
    url = models.URLField(null=True)
    def __str__(self):
        return self.name