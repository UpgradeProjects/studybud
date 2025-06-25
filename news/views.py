from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

@login_required 


def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {
        'news': news,
    })

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
            return redirect('news_home')
    else:
        form = ArticleForm()
    
    return render(request, 'news/create.html', {'form': form})

def news_list(request):
    articles = Articles.objects.all().select_related('faculty', 'theme')
    return render(request, 'news/news_home.html', {'articles': articles})

def news_detail(request, pk):
    article = Articles.objects.select_related('faculty', 'theme').get(pk=pk)
    return render(request, 'news/details_view.html', {'article': article})

