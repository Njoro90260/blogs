from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': '', 'title': ''}
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title here'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,  # Sets the number of visible text lines
                'placeholder': 'Write your post here...'
            }),
        }