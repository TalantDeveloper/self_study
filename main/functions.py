import random

from .models import *


def questions_create(science: Credit, type):
    credit = Credit.objects.get(slug=science.slug)
    questions = credit.questions.all()

    www = random.choices(questions, k=20)
    content = {
        'credit': credit.title,
        'questions': [
            www
        ]
    }


