from django.contrib import admin
from movieapp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate','movie_name','hero','heroine','rating']

admin.site.register(Movie,MovieAdmin)