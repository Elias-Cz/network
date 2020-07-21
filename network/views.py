import datetime

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Post, Like, Follower


def index(request):
    msg = "please log in"
    posts = Post.objects.all()
    if request.method == "POST":
        get_post = request.POST.get('post')
        time_now = datetime.datetime.now()
        time = time_now.strftime("%B %d, %Y")
        print(get_post)
        user = request.user
        likes = 0
        post = Post(post=get_post, user=user, time=time, likes=likes)
        post.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "network/index.html", {
    "posts": posts,
    "msg": msg
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request, username):
    if request.user in Follower.objects.filter(user_followed=request.user):
        follow_status = "Unfollow" # pseudo if request user follow user username follow status = "unfollow"
    else:
        follow_status = "Follow"
    print(username)
    username = get_object_or_404(User, username=username)
    current_user = request.user
    print(current_user)
    posts = Post.objects.filter(user_id=username)
    if request.method == "POST":
        user_followed = request.user
        user_following = username
        follower = Follower(user_followed=user_followed, user_following=user_following)

        return(None)
    return render(request, "network/profile.html", {
    "username": username,
    "posts": posts,
    "follow_status": follow_status
    })
