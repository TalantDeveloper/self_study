from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Option(models.Model):
    title = models.TextField(verbose_name="Title")
    image = models.ImageField(upload_to='./options/', blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.TextField(verbose_name="Title")
    image = models.ImageField(upload_to='./questions/', blank=True, null=True)
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)

    options = models.ManyToManyField(Option, related_name='options', blank=True)
    corrects = models.ManyToManyField(Option, related_name='corrects', blank=True)

    def __str__(self):
        return self.title


class Credit(models.Model):
    title = models.TextField(verbose_name='Title')
    slug = models.CharField(max_length=20, verbose_name='Slug')
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)
    questions = models.ManyToManyField(Question, related_name='questions', blank=True)

    def __str__(self):
        return f"{self.slug} - {self.title}"
