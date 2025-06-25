from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('my_news', views.user, name='user_news')
]
