from django.shortcuts import render
from .models import  Movie
from django.shortcuts import get_object_or_404
from django.http import Http404
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    contex = {
       'movies':movies
    }
    return  render(request,'movies/list.html',contex)

def detail(request,movie_id):
    movie = get_object_or_404(Movie, pk = movie_id)

    context = {
        'movie':movie
    }

    return render(request,'movies/detail.html',context)



    # try:
    # movie = Movie.objects.get(pk = movie_id)
    # except Movie.DoesNotExist;
    # raise Http404(request,'kayıt bulunnamaktadır')

def search(request):
    return  render(request,'movies/search.html')



