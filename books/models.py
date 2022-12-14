from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')  # permission

    def __str__(self):
        return self.title
