from django.shortcuts import render
from news.models import Faculty, NewsTheme, Articles


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

def index(request):
    context = {
        'title': 'Новостной портал',
        'faculty_selected': False,
        'theme_selected': False
    }
    
    faculty_id = request.GET.get('faculty')
    theme_id = request.GET.get('theme')
    
    if faculty_id:
        try:
            selected_faculty = Faculty.objects.get(id=faculty_id)
            context['selected_faculty'] = selected_faculty
            context['faculty_selected'] = True
            
            if theme_id:
                selected_theme = NewsTheme.objects.get(id=theme_id)
                context['selected_theme'] = selected_theme
                context['theme_selected'] = True
                context['news'] = Articles.objects.filter(
                    faculty=selected_faculty,
                    theme=selected_theme
                ).order_by('-date')
            else:
                context['themes'] = NewsTheme.objects.all()
        except (Faculty.DoesNotExist, NewsTheme.DoesNotExist):
            pass
    else:
        context['faculties'] = Faculty.objects.all()
    
    return render(request, 'main/index.html', context)