from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

from .models import Blog_Post

class BlogListView(ListView):

    model = Blog_Post
    template_name = 'blog.html'

# class BlogDetails(ListView):

#     model = Blog_Post
#     template_name = 'Blog_detail.html'
#     context_object_name = 'all_posts_list'  

def BlogDetails(request, id):
  mymember = Blog_Post.objects.get(id=id)
  template = loader.get_template('Blog_detail.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
      
