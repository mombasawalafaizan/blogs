from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
	title = forms.CharField(initial = "Enter title")
	class Meta:
		model = BlogPost
		fields = ['title', 'text']
		labels = {'title':'', 'text': ''}
		widgets = {'text': forms.Textarea(attrs = {'cols' : 80})}