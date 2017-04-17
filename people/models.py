from django.db import models

# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    image = models.ImageField(upload_to = 'person_image', blank=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    description = models.TextField(default='' , null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(default='', null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    role = models.ForeignKey(Role)

    def __str__(self):
        return self.name+' '+self.last_name
