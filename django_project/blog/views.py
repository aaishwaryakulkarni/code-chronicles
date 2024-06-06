from django.shortcuts import render

posts = [
    {
        'author': 'Aish',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted':'June 6 2024'
    },
    {
        'author': 'Shash',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted':'May 31 2024'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
