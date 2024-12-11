from django.urls import path

from .views import register,login,profile,signout

urlpatterns = [
    path("login",login,name="login"),
    path("profile",profile,name="profile"),
    path("logout",signout,name="logout")
]
