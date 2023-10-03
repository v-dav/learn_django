from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
def home(request):
    return render(request, 'depistclic/home.html')


def about(request):
    return render(request, 'depistclic/about.html')


def questions(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'depistclic/home.html', context)
