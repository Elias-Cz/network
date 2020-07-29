import datetime

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator

from .models import User, Post, Like, Follower


def index(request):
    msg = "please log in"
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # New post function
    if request.method == "POST":
        get_post = request.POST.get('post')
        time_now = datetime.datetime.now()
        time = time_now.strftime("%B %d, %Y %H:%M")
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
    # Username of profile currently being used *NOT THE CURRENT USER*
    username = get_object_or_404(User, username=username)
    current_user = request.user
    current_user_following = username.user_following.filter(user_followed=current_user).exists()
    if current_user == username:
        user_self = True
    else:
        user_self = False
    # Check if CURRENT USER follows {username}
    if current_user_following:
        print(current_user, ' follows ', username, '?: ', current_user_following)
        follow_status = "Unfollow"
    else:
        print(current_user, ' follows ', username, '?: ', current_user_following)
        follow_status = "Follow"
    # Posts for users profile
    posts = Post.objects.filter(user_id=username).order_by('-id')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # Followers/following count
    followers = username.user_following.all().count()
    following = username.user_followed.all().count()
    # Following a user
    if request.method == "POST" and not current_user_following:
        user_followed = current_user
        user_following = username
        f = Follower(user_followed=user_followed, user_following=user_following)
        f.save()
        print(user_followed, ' followed ', user_following)

        return render(request, "network/profile.html", {
        "username": username,
        "posts": posts,
        "follow_status": follow_status,
        "followers": followers,
        "following": following
        })

    # Unfollowing a user
    elif request.method == "POST" and current_user_following:
        user_followed = current_user
        user_following = username
        Follower.objects.filter(user_followed=user_followed, user_following=user_following).delete()

        return render(request, "network/profile.html", {
        "username": username,
        "posts": posts,
        "follow_status": follow_status,
        "followers": followers,
        "following": following
        })

    return render(request, "network/profile.html", {
    "username": username,
    "posts": posts,
    "follow_status": follow_status,
    "followers": followers,
    "following": following,
    "user_self": user_self
    })

def following_view(request):
    current_user = request.user
    # Gathering current user following list (as obj)
    current_user_follows = current_user.user_followed.all()
    following = []
    for follows in current_user_follows:
        user = follows.user_following
        if user in following:
            pass
        else:
            following.append(user)
    # Posts are filtered out on template
    posts_list = Post.objects.all()
    posts = []
    for post in posts_list:
        if post.user in following:
            posts.append(post)
        else:
            pass
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "network/following.html",{
    "posts": posts,
    "following": following
    })
