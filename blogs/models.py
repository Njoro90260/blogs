from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """Model for the Blog Post."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.title}: {self.text[:50]}..."


