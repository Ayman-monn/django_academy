from django.db import models
from django.contrib.auth.models import User 
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _ 
class Course(models.Model):
    name = models.CharField(_('Name'),max_length=155) 
    image = models.ImageField(_('Image'),upload_to='courses/')
    price = models.FloatField(_('Price')) 
    short_description = models.TextField(_('Short_description')) 
    description = models.TextField(_('Description'))
    info = models.TextField(_('Info'))
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name 
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class Section(models.Model): 
    name = models.CharField(_('Name') ,max_length=155) 

    # relational fields 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')


    
    def __str__(self): 
        return self.name 
    

class Lesson(models.Model): 
    name = models.CharField(_('Name'),max_length=155) 
    description = models.TextField(_('Description'),max_length=500, null=True, blank=True) 
    video = models.FileField(_('Video'),upload_to='lessons/') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    # relational fields 
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self): 
        return self.name 
    

class Comment(models.Model): 
    body = RichTextUploadingField(_('Body')) 
    # relational fields 
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.PROTECT)


    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self): 
        return self.lesson.name + '>' + self.user.username 
    




class StudentCourses(models.Model):     
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 





