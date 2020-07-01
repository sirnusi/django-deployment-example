from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    latest = Post.objects.order_by('timestamp')[0:3]
    context = {'latest':latest}
    return render(request, 'blog_application/index.html', context)

def about(request):
    return render(request, 'blog_application/aboutme.html')

def politics(request):
    return render(request, 'blog_application/politics.html')

def business(request):
    return render(request, 'blog_application/business.html')

def technology(request):
    return render(request, 'blog_application/tech.html')

def sports(request):
    return render(request, 'blog_application/sports.html')

def entertainment(request):
    return render(request, 'blog_application/entertain.html')