from django.shortcuts import render
import pymysql
from TestModel import models

 
def hello(request):
    phone_list = models.Test.objects.all()
    return render(request, 'phone.html', {"phone_list":phone_list})


def movie(request):
    movie_list = models.Movie.objects.all()
    return render(request, 'movie.html', {"movie_list":movie_list})

   

