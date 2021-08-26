from django.urls import path
from BasicApp import views

app_name = 'BasicApp'

urlpatterns = [
path('registration/', views.registration, name = 'registration'),
path('login/', views.user_login, name = 'login')
]
