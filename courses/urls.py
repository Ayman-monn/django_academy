from django.urls import path 
from . import views



urlpatterns = [
    path('', views.courses_list, name="Courses_list"), 
    path('course/detail/<int:cid>/', views.course_detial, name="Course_detail"), 
    path('course/sections/<int:cid>/', views.sections, name="Course_section"), 
    path('course/section/lessons/<int:sid>/', views.lesson_list, name="Course_section_lessons"), 
    path('course/section/lessons/lesson/<int:lid>/', views.lesson, name="Lesson"), 
]