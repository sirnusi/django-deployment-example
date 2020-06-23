from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog_application/index.html')

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