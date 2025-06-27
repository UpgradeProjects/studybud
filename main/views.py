from django.shortcuts import render

def user(request):
    data = {
        'title': 'Ваши новости'
    }
    return render(request, 'news/user_news.html', data)


