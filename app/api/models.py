from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    date = models.DateTimeField(auto_now = False)
    tags = models.ManyToManyField('Tag')
    keywords = models.ManyToManyField('Keywords')
    name = models.CharField(max_length = 255)
    description = RichTextUploadingField(null = True)
    image = models.ImageField(null = True, upload_to = 'images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Tag(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Keywords(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Ключ. слово"
        verbose_name_plural = "Ключ. слова"
