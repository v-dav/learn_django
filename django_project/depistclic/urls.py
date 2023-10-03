from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='depistclic-home'),
    path('about/', views.about, name='depistclic-about'),
    path('questions/', views.questions, name='depistclic-questions')
]
