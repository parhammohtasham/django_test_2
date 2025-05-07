from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Blog
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model= Blog
    template_name='blog/list.html'
    context_object_name='blog_list'

class BlogDetailView(DetailView):
    model=Blog
    template_name='blog/detail.html'
    context_object_name='blog_detail'

class BlogCreateView(CreateView):
    model=Blog
    template_name='blog/new.html'
    fields=['title','body','author']

class BlogUpdateView(UpdateView):
    model=Blog
    template_name='blog/edit.html'
    fields=['title','body']

class BlogDeleteView(DeleteView):
    model=Blog
    template_name='blog/delete.html'
    success_url=reverse_lazy('blog_list')
