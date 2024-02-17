from django.shortcuts import render
from .models import Credit, Question, Option


def welcome(request):
    credits = Credit.objects.all()
    content = {
        'credits': credits
    }
    return render(request, 'main/welcome.html', content)


def credit_view(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        credit = Credit.objects.get(slug=slug)
        content = {
            'credits': credit,
        }
        return render(request, 'main/welcome.html', content)

    return render(request, 'main/welcome.html')

