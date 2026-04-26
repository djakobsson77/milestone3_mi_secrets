from django.db import models

# Create your models here.

class Island(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
    

class PirateItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name