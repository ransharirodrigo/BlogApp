from django.urls import path

from .views import add_new_blog_post

urlpatterns = [
    path('create',add_new_blog_post,name="create_blog"),
   
]
