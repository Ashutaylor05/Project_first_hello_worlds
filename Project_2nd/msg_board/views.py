from django.shortcuts import render

from django.views.generic import ListView 
from .models import msg_Post

class List_msg(ListView):
    model = msg_Post
    template_name = "home.html"
    context_object_name = 'all_posts_list'