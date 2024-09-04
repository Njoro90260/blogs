from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': '', 'title': ''}
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title here'}),
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': 'Write your post here...'})
            }