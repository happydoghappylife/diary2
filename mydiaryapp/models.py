from django.db import models

class Mydiary(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to = 'img/', blank=True, null=True)

def __str__(self):
    return self.title