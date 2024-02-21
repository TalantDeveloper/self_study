from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Option(models.Model):
    """Options"""
    title = models.TextField(verbose_name="Title")
    image = models.ImageField(upload_to='./options/', blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def count_options(self):
        return Option.objects.count()


class Question(models.Model):
    """Questions"""
    title = models.TextField(verbose_name="Title")
    image = models.ImageField(upload_to='./questions/', blank=True, null=True)
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)

    options = models.ManyToManyField(Option, related_name='options', blank=True)
    corrects = models.ManyToManyField(Option, related_name='corrects', blank=True)

    def __str__(self):
        return self.title

    @property
    def count_questions(self):
        return Question.objects.count()

    @property
    def get_options(self):
        ops = [option.title for option in self.options.all()]
        return {'count': self.options.all().count(), 'options': ops}

    @property
    def get_corrects(self):
        cors = [correct.title for correct in self.corrects.all()]
        return {'count': self.corrects.all().count(), 'corrects': cors}


class Credit(models.Model):
    """Credit"""
    title = models.TextField(verbose_name='Title')
    slug = models.CharField(max_length=20, verbose_name='Slug')
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)
    questions = models.ManyToManyField(Question, related_name='questions', blank=True)

    def __str__(self):
        return f"{self.slug} - {self.title}"

    @property
    def count_credits(self):
        return Credit.objects.count()

    @property
    def get_questions(self):
        quess = [question.title for question in self.questions.all()]
        return {'count': self.questions.all().count(), 'questions': quess}

