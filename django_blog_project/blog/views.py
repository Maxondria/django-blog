from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Post
from .mixins import TestFunctionMixin


def home(request):
    context = {
        'posts': Post.find_all()
    }
    return render(request, 'blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    # template_name -> <app>/<model>_detail.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # <app>/<model>_form.html


class PostUpdateView(LoginRequiredMixin, TestFunctionMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # <app>/<model>_form.html


class PostDeleteView(LoginRequiredMixin, TestFunctionMixin,  UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    context_object_name = 'post'
    # <app>/<model>_confirm_delete.html


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
