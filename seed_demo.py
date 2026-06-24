import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialmedia.settings')

import django

django.setup()

from django.contrib.auth.models import User
from feed.models import Comment, Follow, Like, Post, Profile


def create_user(username, email, bio, password='DemoPass123'):
    user, created = User.objects.get_or_create(username=username, defaults={'email': email})
    if created:
        user.set_password(password)
        user.save()
    Profile.objects.get_or_create(user=user, defaults={'bio': bio})
    profile = user.profile
    profile.bio = bio
    profile.save()
    return user

alice = create_user('alice', 'alice@example.com', 'Frontend enthusiast building clean UI experiences.')
bob = create_user('bob', 'bob@example.com', 'Backend developer who loves APIs and databases.')
charlie = create_user('charlie', 'charlie@example.com', 'Full-stack learner documenting the journey.')

post1, _ = Post.objects.get_or_create(author=alice, content='Excited to share my first post on CodeAlpha Social!')
post2, _ = Post.objects.get_or_create(author=bob, content='Today I finished the backend routes for comments and likes.')
post3, _ = Post.objects.get_or_create(author=charlie, content='Working on a beautiful profile page and responsive layout.')

Comment.objects.get_or_create(post=post1, author=bob, content='Nice start! The UI looks great already.')
Comment.objects.get_or_create(post=post2, author=alice, content='Love the progress. API + database combo is solid.')
Comment.objects.get_or_create(post=post3, author=bob, content='Can’t wait to see the final version live.')

Like.objects.get_or_create(user=alice, post=post2)
Like.objects.get_or_create(user=bob, post=post1)
Like.objects.get_or_create(user=charlie, post=post1)
Like.objects.get_or_create(user=charlie, post=post2)

Follow.objects.get_or_create(follower=alice, following=bob)
Follow.objects.get_or_create(follower=alice, following=charlie)
Follow.objects.get_or_create(follower=bob, following=alice)
Follow.objects.get_or_create(follower=charlie, following=alice)

print('Demo data ready.')
