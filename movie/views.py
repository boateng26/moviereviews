from urllib import request
from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def homeView(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movie_obj = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movie_obj = Movie.objects.all()
    context = {
        'searchTerm': searchTerm,
        'movies': movie_obj
    }
    return render(request, 'movie/home.html', context)


def movieDetailView(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie = movie).order_by('-date')
    context = {
        'movie': movie,
        'reviews': reviews
    }
    return render(request, 'movie/movie-detail.html', context)

@login_required
def createReview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'GET':
        context = {
            'form': ReviewForm(),
            'movie': movie,
            
        }
        return render(request, 'movie/create-review.html', context)

    else:
        try:
            form = ReviewForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.movie = movie
                instance.save()
                return redirect('movie:movie-detail', instance.movie.id)
        except ValueError:
            context = {
                'form': ReviewForm(),
                'movie': movie,
                'error': 'bad data passed in'
            }
            return render(request, 'movie/create-review.html', context)

@login_required
def updateReview(request, review_id):
    review = get_object_or_404(Review, pk= review_id, user=request.user)
    if request.method == 'GET':
        context = {
            'review': review,
            'form': ReviewForm(instance=review)
        }
        return render(request, 'movie/update-review.html', context)

    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid:
                instance = form.save()
                return redirect('movie:movie-detail', instance.movie.id)
        except ValueError:
            context = {
                'form': ReviewForm(instance=review),
                'review': review,
                'error': 'bad data passed in'
            }
            return render(request, 'movie/create-review.html', context)

@login_required
def deleteView(request, review_id):
    review = get_object_or_404(Review, pk= review_id, user= request.user.id)
    if request.method == 'POST':
        review.delete()
        return redirect('movie:movie-detail', review.movie.id)
    context = {
        'review': review
    }
    return render(request, 'movie/delete-review.html', context)
    