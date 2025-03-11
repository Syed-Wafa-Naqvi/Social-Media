from django.urls import path
from .views import post_list_create, post_detail, like_post, comment_post
from .views import index, login_view

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('posts/', post_list_create, name='post-list-create'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/<int:post_id>/like/', like_post, name='like-post'),
    path('posts/<int:post_id>/comment/', comment_post, name='comment-post'),
]