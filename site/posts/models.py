from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    text=models.TextField()

    def __str__(self):
        return self.text[:]
    
    def get_absolute_url(self):
        return reverse("posts")
    


