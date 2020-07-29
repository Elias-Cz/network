
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    # ForeignKey('User', on_delete=models.CASCADE, related_name='user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auth")
    post = models.CharField(max_length = 140)
    likes = models.IntegerField(default=0, blank=True, null=True)
    time = models.CharField(max_length = 40, null=True)
    class Meta:

        ordering = ['-time']

    def __str__(self):
        return f"{self.post} by {self.user} {self.likes} Likes at {self.time}"

class Like(models.Model):
    user_like = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_origin")

class Follower(models.Model):
    # User who is FOLLOWING
    user_following = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_following")
    # User who is gaining a follower
    user_followed = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_followed")

    def __str__(self):
        return f"{self.user_following} followed by {self.user_followed}"
