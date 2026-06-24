from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CommentForm, LoginForm, PostForm, ProfileForm, RegisterForm
from .models import Follow, Like, Post, Profile


def ensure_profile(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile


def enrich_posts(posts, user=None):
    for post in posts:
        post.like_count = post.likes.count()
        post.comment_count = post.comments.count()
        post.is_liked = user.is_authenticated and Like.objects.filter(user=user, post=post).exists() if user else False
        post.comment_form = CommentForm()
    return posts


def home(request):
    posts = enrich_posts(
        Post.objects.select_related('author').prefetch_related('comments__author', 'likes'),
        request.user if request.user.is_authenticated else None,
    )
    suggested_users = []
    if request.user.is_authenticated:
        ensure_profile(request.user)
        followed_ids = list(
            Follow.objects.filter(follower=request.user).values_list('following_id', flat=True)
        )
        suggested_users = User.objects.exclude(id__in=followed_ids + [request.user.id]).annotate(
            post_count=Count('posts')
        )[:5]
    context = {
        'posts': posts,
        'post_form': PostForm(),
        'suggested_users': suggested_users,
    }
    return render(request, 'feed/home.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            Profile.objects.create(user=user, bio=form.cleaned_data.get('bio', ''))
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'feed/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
    else:
        form = LoginForm(request)
    return render(request, 'feed/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post published.')
    return redirect('home')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added.')
    next_url = request.POST.get('next_url') or reverse('home')
    return HttpResponseRedirect(next_url)


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
    else:
        Like.objects.create(user=request.user, post=post)
    next_url = request.POST.get('next_url') or reverse('home')
    return HttpResponseRedirect(next_url)


def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    profile = ensure_profile(profile_user)
    posts = enrich_posts(
        Post.objects.filter(author=profile_user).select_related('author').prefetch_related('comments__author', 'likes'),
        request.user if request.user.is_authenticated else None,
    )
    follower_count = Follow.objects.filter(following=profile_user).count()
    following_count = Follow.objects.filter(follower=profile_user).count()
    is_following = False
    if request.user.is_authenticated and request.user != profile_user:
        is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()
    return render(
        request,
        'feed/profile.html',
        {
            'profile_user': profile_user,
            'profile': profile,
            'posts': posts,
            'follower_count': follower_count,
            'following_count': following_count,
            'is_following': is_following,
        },
    )


@login_required
def toggle_follow(request, username):
    target_user = get_object_or_404(User, username=username)
    if target_user != request.user:
        relation = Follow.objects.filter(follower=request.user, following=target_user)
        if relation.exists():
            relation.delete()
            messages.info(request, f'You unfollowed {target_user.username}.')
        else:
            Follow.objects.create(follower=request.user, following=target_user)
            messages.success(request, f'You are now following {target_user.username}.')
    return redirect('profile', username=target_user.username)


@login_required
def edit_profile(request):
    profile = ensure_profile(request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile, initial={'email': request.user.email})
    return render(request, 'feed/edit_profile.html', {'form': form})
