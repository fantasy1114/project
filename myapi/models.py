from django.db import models
class Hero(models.Model):
    # thumb = models.ImageField(upload_to='hero_images')
    thumb = models.TextField(max_length=10000000)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=60)
    designation = models.CharField(max_length=60)
    def __str__(self):
        return self.name