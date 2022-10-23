from django.urls import path
from .views import newsView

app_name = 'news'
urlpatterns = [
    path('', newsView, name='news-home')
]
