from django.shortcuts import render
from .models import Course, Section, Lesson, Comment

def index(request): 
    return render(request, 'index.html') 
