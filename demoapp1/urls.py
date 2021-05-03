from django.urls import path
from demoapp1 import views

urlpatterns = [
    path('about/', views.about_page)
]