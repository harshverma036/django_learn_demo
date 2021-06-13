from django.urls import path
from demoapp import views

urlpatterns = [
    path('home/', views.home_page),
    path('password/', views.password_validate)
]