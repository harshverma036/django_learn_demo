from django.urls import path
from demoapp import views

urlpatterns = [
    path('home/', views.home_page)
]