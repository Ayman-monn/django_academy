from django.shortcuts import render
from .models import Course, Section, Lesson, Comment


def courses_list(request):
    courses = Course.objects.all() 
    return render(request, 'index.html',{
        'courses':courses
    })

def course_detial(request, cid): 
    course = Course.objects.get(pk=cid) 
    return render(request, 'course_detail.html',{
        'course':course 
    })

def sections(request, cid): 
    sections = Section.objects.select_related('course').filter(course=cid) 
    return render(request, 'courses/sections.html', {
        'sections':sections
    })

def lesson_list(request, sid): 
    lessons = Lesson.objects.select_related('section').filter(section=sid)
    return render(request, 'courses/lessons_list.html',{
        'lessons':lessons
    })

def lesson(request, lid): 
    lesson = Lesson.objects.get(pk=lid)
    return render(request, 'courses/lesson.html', {
        'lesson':lesson 
    })