from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Blog
# Create your views here.

class BlogListView(ListView):
    model= Blog
    template_name='blog/list.html'
    context_object_name='blog_list'

class BlogDetailView(DetailView):
    model=Blog
    template_name='blog/detail.html'
    context_object_name='blog_detail'