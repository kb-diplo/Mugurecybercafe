from django import forms
from django.utils import timezone
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'excerpt', 'featured_image', 'status', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter blog post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your blog post content here...'
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief summary of the post (optional)'
            }),
            'featured_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'published_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default published date to now if creating new post
        if not self.instance.pk and not self.initial.get('published_date'):
            self.fields['published_date'].initial = timezone.now()
    
    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        published_date = cleaned_data.get('published_date')
        
        # If status is published, ensure published_date is set
        if status == 'published' and not published_date:
            cleaned_data['published_date'] = timezone.now()
        
        return cleaned_data
