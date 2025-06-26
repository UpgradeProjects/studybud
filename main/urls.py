from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name="about"),
    path('my_news', views.user, name='user_news')
]
