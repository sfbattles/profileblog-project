from django.urls import path
from blog import views as blog_views

urlpatterns = [   
    path('', blog_views.blogs, name='blogs'), 
    path('<int:blog_id>', blog_views.blog_details, name="blog_details")  #blog_views is what I called my import
    #blog_details is the function it will call in the views.py file            
]
