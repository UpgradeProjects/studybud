from django.contrib import admin
from .models import Faculty, Articles,Topic

admin.site.register(Faculty)
admin.site.register(Topic)
admin.site.register(Articles)