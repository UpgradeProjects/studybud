from django.shortcuts import render, redirect
from .models import Faculty, NewsTheme, Articles, Topic
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

@login_required 


def news_home(request):
    news_list = Articles.objects.all().order_by('-date')
    paginator = Paginator(news_list, 4)  
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, 'news/news_home.html', {'news': news})

class NewDetailView(DetailView):
    model = Articles
    template_name = 'news/user_news.html'
    context_object_name = 'article'


class NewDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticleForm

class NewDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            print(f"New post created by: {request.user.username} (ID: {request.user.id})")
            return redirect('user_news')
    else:
        form = ArticleForm()
    return render(request, 'news/create.html', {'form': form})

def news_list(request):
    articles = Articles.objects.all().select_related('faculty', 'theme')
    return render(request, 'news/news_home.html', {'articles': articles})

def news_detail(request, pk):
    article = Articles.objects.select_related('faculty', 'theme').get(pk=pk)
    return render(request, 'news/details_view.html', {'article': article})

def theme_list(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    themes = NewsTheme.objects.all()
    return render(request, 'news/theme_list.html', {
        'faculty': faculty,
        'themes': themes
    })

def faculty_theme_news(request, faculty_id, theme_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    theme = get_object_or_404(NewsTheme, pk=theme_id)
    news = Articles.objects.filter(faculty=faculty, theme=theme).order_by('-date')
    
    return render(request, 'news/faculty_theme_news.html', {
        'faculty': faculty,
        'theme': theme,
        'news': news
    })

def home(request):
    faculties = Faculty.objects.all()
    
    return render(request, 'news/home.html', {'faculties': faculties})

def user_news(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user_posts = Articles.objects.filter(
        author=request.user
    ).select_related('faculty', 'theme').order_by('-date')
    
    paginator = Paginator(user_posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'news/user_news.html', {
        'page_obj': page_obj, 
        'user': request.user
    })

