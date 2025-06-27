from django.urls import path
from . import views

urlpatterns = [
    path('my_news', views.user, name='user_news')
]