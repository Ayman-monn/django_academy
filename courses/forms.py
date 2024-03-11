from django import forms
from courses.models import Comment 
from ckeditor.widgets import CKEditorWidget



attrs = {'class':'form-control'}


class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment
        fields = ['body']
        widgets={
            'body': forms.CharField(widget=CKEditorWidget(attrs=attrs))
        }
        
