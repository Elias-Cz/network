from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    # ForeignKey('User', on_delete=models.CASCADE, related_name='user')
    user = models.CharField(max_length = 40)
    post = models.CharField(max_length = 140)
    likes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.post} by {self.user} {self.likes} Likes"
