from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class NewsTheme(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Articles(models.Model):
    title = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(NewsTheme, on_delete=models.SET_NULL, null=True)
    full_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:  
        verbose_name = 'Новость'         
        verbose_name_plural = 'Новости'  

