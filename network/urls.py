
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following_view, name="following"),
    path("<str:username>", views.profile, name="profile"),
    path("post/<int:post_id>/<str:text>", views.post_edit, name="post_edit"),
    path("like/<int:post_id>/<int:count>", views.like, name="like")

]
