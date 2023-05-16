from django.db import models

class News(models.Model):
    date = models.DateTimeField(auto_now = False)
    tags = models.ManyToManyField('Tag')
    keywords = models.ManyToManyField('Keywords')
    name = models.CharField(max_length = 255)
    description = models.TextField(null = True)
    image = models.ImageField(null = True, upload_to = 'images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length = 255)

class Keywords(models.Model):
    name = models.CharField(max_length = 255)
