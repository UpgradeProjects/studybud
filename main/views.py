from django.shortcuts import render
# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some','Hello','Bye'],
        'obj': {
            'car': 'Lambo',
            'skate': 'cheap',
            'brain': 'tasty'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def user(request):
    data = {
        'title': 'Ваши новости'
    }
    return render(request, 'main/user_news.html', data)

