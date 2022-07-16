from django.shortcuts import render, redirect, get_list_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# def home(request):
#     context = {
#         'page_name':home.__name__,
#         'posts':Post.objects.all()
#     }
#     return render(request, 'Blog/home.html', context)


def about(request):
    context = {
        'page_name':about.__name__
    }
    return render(request, 'Blog/about.html', context)

class MyPostList(ListView):
    model = Post
    template_name = 'Blog/my-posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class ResentPost(ListView):
    model = Post
    template_name = 'Blog/resent-posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(date_posted__gte=datetime.now() - timedelta(days=1))



class PostList(ListView):
    model = Post
    template_name = 'Blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostListAuthor(ListView):
    model = Post
    template_name = 'Blog/post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=User.objects.get(username=self.kwargs.get('username')))


class PostDetail(DetailView):
    model = Post
    template_name = "Blog/post-detail.html"
    context_object_name = 'post'
    

class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    # queryset = Post.objects.all() <can be replaced with above>
    fields = ['title', 'content']
    template_name = 'Blog/post-create.html'
    # success_url = reverse_lazy('blog-home')

    def get_success_message(self, cleaned_data):
        return f"post {cleaned_data['title']} is written by {self.request.user.username}"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'Blog/post-update.html' 

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'Blog/post-delete.html'
    success_url = reverse_lazy('blog-post-myposts')

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False
