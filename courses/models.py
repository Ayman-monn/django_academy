from django.db import models
from django.contrib.auth.models import User 

class Course(models.Model):
    name = models.CharField(max_length=155) 
    image = models.ImageField(upload_to='courses/')
    price = models.FloatField() 
    short_description = models.TextField() 
    description = models.TextField()
    info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name 



class Section(models.Model): 
    name = models.CharField(max_length=155) 

    # relational fields 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    

    
    def __str__(self): 
        return self.name 
    

class Lesson(models.Model): 
    name = models.CharField(max_length=155) 
    description = models.TextField(max_length=500, null=True, blank=True) 
    video = models.FileField(upload_to='lessons/') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    # relational fields 
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name 
    

class Comment(models.Model): 
    body = models.TextField() 
    image = models.ImageField(upload_to='comment/') 
    # relational fields 
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.PROTECT)


    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self): 
        return self.lesson.name + '>' + self.user.username 
    




class StudentCourses(models.Model):     
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 




