from django.shortcuts import render
from django.views.generic import  ListView
from django.views.generic.edit import CreateView
from .models import Post
# Create your views here.

class PostPageView(ListView):
    model=Post
    template_name='posts/list.html'
    context_object_name='posts'

class NewPostPageView(CreateView):
    model=Post
    template_name='posts/new.html'
    fields=['text']
    