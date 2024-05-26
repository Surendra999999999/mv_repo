from django.shortcuts import render
from movieapp.models import Movie
from movieapp.forms import MovieForm
# Create your views here.
def movie_index(request):
    return render(request,'movieapp/index.html')
def movie_list(request):
    movie_list = Movie.objects.all()
    return render(request,'movieapp/movie_list.html',{'movie_list':movie_list})


def movie_form(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return movie_index(request)
    return render(request,'movieapp/form.html',{"form":form})
