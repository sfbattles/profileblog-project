from django.shortcuts import render, get_object_or_404
from .models import Blog
from jobs.models import Job

# Create your views here.
def blogs(request):
    context = {
        'blogs' : Blog.objects.all(),
        'jobs' : Job.objects.all()
    }
    return render(request,'blog/blogs.html', context)
    
def blog_details (request,blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)  #gets the object with the primary key equal to BlogID    
    return render(request,"blog/blog_details.html", {'blog':blog_detail})