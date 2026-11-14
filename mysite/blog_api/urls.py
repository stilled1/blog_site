from django.urls import path
from . import views
from .views import PostList,PostDetail, UserPostList

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('user/<int:id>/', UserPostList.as_view())
]