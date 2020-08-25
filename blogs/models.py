from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """The blog which will be posted"""
    title = models.CharField(max_length=50) 
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title.upper()