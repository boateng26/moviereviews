from django.urls import path
from .views import signupView,loginView,logoutaccount

app_name = 'accounts'
urlpatterns = [
   path('signup/', signupView, name='signup'),
   path('login/', loginView, name='login'),
   path('logout/', logoutaccount, name='logout')
]
