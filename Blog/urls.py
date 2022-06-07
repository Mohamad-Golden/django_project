from Blog.models import Post
from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('home/', views.PostList.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='blog-post'),
    path('post/new/', views.PostCreate.as_view(), name='blog-post-create'),
    path('post/update/<int:pk>/', views.PostUpdate.as_view(), name='blog-post-update'),
    path('post/delete/<int:pk>/', views.PostDelete.as_view(), name='blog-post-delete'),
    path('post/myposts/', views.MyPostList.as_view(), name='blog-post-myposts'),
    path('post/resent/', views.ResentPost.as_view(), name='blog-post-resent'),
    path('post/<str:username>/', views.PostListAuthor.as_view(), name='blog-post-author')
]