from django import forms
from django import forms
from .models import Articles

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'faculty', 'theme', 'full_text'] 
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'faculty': forms.Select(attrs={
                'class': 'form-control'
            }),
            'theme': forms.Select(attrs={
                'class': 'form-control'
            }),
            'full_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }