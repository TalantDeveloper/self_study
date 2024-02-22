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


assas = [
    {
        'title': 'Bilmaddimmi bilmadim?',
        'image': '',
        'options': [
            {
                'title': 'Bildim',
                'image': '',
            },
            {
                'title': 'bilmadim',
                'image': '',
            },
            {
                'title': 'sasa',
                'image': '',
            },
            {
                'title': 'ssaasasdaa',
                'image': '',
            }
        ]
    },
    {
        'title': 'Bilmaddimmi bilmadim?',
        'image': '',
        'options': [
            {
                'title': 'Bildim',
                'image': '',
            },
            {
                'title': 'bilmadim',
                'image': '',
            },
            {
                'title': 'sasa',
                'image': '',
            },
            {
                'title': 'ssaasasdaa',
                'image': '',
            }
        ]
    }, {
        'title': 'Bilmaddimmi bilmadim?',
        'image': '',
        'options': [
            {
                'title': 'Bildim',
                'image': '',
            },
            {
                'title': 'bilmadim',
                'image': '',
            },
            {
                'title': 'sasa',
                'image': '',
            },
            {
                'title': 'ssaasasdaa',
                'image': '',
            }
        ]
    },
    {
        'title': 'Bilmaddimmi bilmadim?',
        'image': '',
        'options': [
            {
                'title': 'Bildim',
                'image': '',
            },
            {
                'title': 'bilmadim',
                'image': '',
            },
            {
                'title': 'sasa',
                'image': '',
            },
            {
                'title': 'ssaasasdaa',
                'iamge': '',
            }
        ]
    }
]


def credit_questions(credit_id, num=20):
    questions = Credit.objects.get(id=credit_id).questions.all()
    titles = [question.title for question in questions]
    print(f"dastlab: {titles}")
    random.shuffle(titles)
    print(f"o'zgargani: {titles}")
    return titles


def credit_versions(titles):
    versions = []
    for title in titles:
        vers = {}
        question = Question.objects.get(title=title)
        vers['question'] = question
        options = [option.title for option in question.options.all()]
        random.shuffle(options)
        vers['options'] = options
        versions.append(vers)
    return versions

