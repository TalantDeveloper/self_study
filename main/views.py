import random

from django.shortcuts import render
from .models import Credit, Question, Option
from .functions import credit_versions, credit_questions


def welcome(request):
    if request.method == 'POST':
        title = request.POST['title']
        credits = Credit.objects.filter(title=title)
        return render(request, 'main/welcome.html', {'credits': credits})
    else:
        credits = Credit.objects.all()
    content = {
        'credits': credits
    }
    return render(request, 'main/welcome.html', content)


def credit_view(request):
    questions = Question.objects.all()
    aasal = []
    for question in questions:
        title = question.title
        image = ''
        if question.image:
            image = question.image.url
        options = []
        for option in question.options.all():
            op_title = option.title
            op_image = ''
            if option.image:
                op_image = option.image.url
            options.append(op_title)
        print(f"{title} - {options}")
        aasal.append({'title': title, 'image': image, 'options': options})
    for asal in aasal:
        print(asal['title'], asal['options'])

    # if request.method == 'POST':
    #     slug = request.POST.get('slug')
    #     credit = Credit.objects.get(slug=slug)
    #     content = {
    #         'credits': credit,
    #         'questions': random.shuffle(aasal),
    #     }
    #     return render(request, 'main/credit.html', content)
    content = {
        'questions': aasal,
    }
    return render(request, 'main/credit.html', content)


def credit_edit(request, id):
    credit = Credit.objects.get(id=id)
    content = {
            'credit': credit,
            'versions': credit_versions(credit_questions(id)),
    }
    return render(request, 'main/credit_edit.html', content)




