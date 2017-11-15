# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class PostView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    model = Post

class DetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post


class PostMixin(object):
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.published_date = timezone.now()
        return super(PostMixin, self).form_valid(form)


class PostCreate(PostMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostUpdate(PostMixin, UpdateView):
    """ 
    """