from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
# Create your views here.
def home(request):
    #return render(request, 'home.html', {'name':'Yoyo'})
    searchTerm= request.GET.get('searchMovie')
    if searchTerm:
        movies= Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies= Movie.objects.all()
    return render(request, 'home.html', {'name':'Juan Pablo' ,'searchTerm': searchTerm, 'movies': movies})

def about(request):
    return render(request, 'about.html')

def statistics_view(request):
    matplotlib.use('Agg')

    # ---------- GRÁFICA 1: Películas por año ----------
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    movie_counts_by_year = {}
    for year in years:
        if year:
            movies_in_year = Movie.objects.filter(year=year)
        else:
            movies_in_year = Movie.objects.filter(year__isnull=True)
            year = "None"
        count = movies_in_year.count()
        movie_counts_by_year[str(year)] = count

    plt.figure(figsize=(8, 5))
    plt.bar(movie_counts_by_year.keys(), movie_counts_by_year.values(), color='skyblue')
    plt.title('Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=90)
    plt.tight_layout()

    buffer1 = io.BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    plt.close()
    graphic_year = base64.b64encode(buffer1.getvalue()).decode('utf-8')
    buffer1.close()

    # ---------- GRÁFICA 2: Películas por género ----------
    all_movies = Movie.objects.all()
    movie_counts_by_genre = {}

    for movie in all_movies:
        if movie.genre:
            first_genre = movie.genre.split(',')[0].strip()
            movie_counts_by_genre[first_genre] = movie_counts_by_genre.get(first_genre, 0) + 1
        else:
            movie_counts_by_genre["Unknown"] = movie_counts_by_genre.get("Unknown", 0) + 1

    plt.figure(figsize=(8, 5))
    plt.bar(movie_counts_by_genre.keys(), movie_counts_by_genre.values(), color='lightgreen')
    plt.title('Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    plt.close()
    graphic_genre = base64.b64encode(buffer2.getvalue()).decode('utf-8')
    buffer2.close()

    # ---------- Renderizar ambas en la misma plantilla ----------
    return render(request, 'statistics.html', {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre
    })
