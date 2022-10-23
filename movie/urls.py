"""moviereviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import homeView, movieDetailView, createReview, updateReview, deleteView

app_name = 'movie'
urlpatterns = [
    path('', homeView, name='home'),
    path('movie-detail/<int:movie_id>', movieDetailView, name='movie-detail'),
    path('create-review/<int:movie_id>', createReview, name='create-review'),
    path('update-review/<int:review_id>', updateReview, name='update-review'),
    path('delete-review/<int:review_id>', deleteView, name='delete-review'),
]
