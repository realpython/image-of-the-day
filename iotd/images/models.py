from django.db import models

# Create your models here.
class FeaturedImage(models.Model):

    name = models.CharField(max_length=200)
    tagline = models.TextField()
    uploaded = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="") 
