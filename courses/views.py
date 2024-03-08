from django.shortcuts import redirect, render

from academy_project import settings
from .models import Course, Section, Lesson, Comment, StudentCourses
from django.contrib.auth.decorators import login_required 

def courses_list(request):
    query = request.GET.get('query', '')
    where = {}
    if query: 
        where['name__icontains'] = query
        courses = Course.objects.filter(**where) 
    else: 
        courses = Course.objects.all() 
    return render(request, 'index.html',{
        'courses':courses
    })

def course_detial(request, cid): 
    course = Course.objects.get(pk=cid) 
    return render(request, 'course_detail.html',{
        'course':course, 
        'public_key': settings.STRIPE_PUBLIC_KEY
    })


@login_required 
def my_courses(request): 
    courses = StudentCourses.objects.select_related('user', 'course').filter(user=request.user) 

    return render(request, 'courses/my_courses.html', {
        'courses':courses
    })

@login_required
def sections(request, cid):
    course = Course.objects.get(pk=cid) 
    student = StudentCourses.objects.filter(user = request.user, course = course)
    if not student: 
        return redirect('Courses_list')
    sections = Section.objects.select_related('course').filter(course=cid) 
    return render(request, 'courses/sections.html', {
        'sections':sections
    })


@login_required
def lesson_list(request, sid): 
    course = Course.objects.get(section=sid) 
    student = StudentCourses.objects.filter(user = request.user, course = course)
    if not student: 
        return redirect('Courses_list')
    lessons = Lesson.objects.select_related('section').filter(section=sid)
    return render(request, 'courses/lessons_list.html',{
        'lessons':lessons
    })



@login_required
def lesson(request, lid): 
    course = Course.objects.get(lesson=lid) 
    student = StudentCourses.objects.filter(user = request.user, course = course)
    if not student: 
        return redirect('Courses_list')
    lesson = Lesson.objects.get(pk=lid)
    return render(request, 'courses/lesson.html', {
        'lesson':lesson 
    })