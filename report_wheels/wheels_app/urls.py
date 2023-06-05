from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login_page"),
    path("logout_user/", views.logout_user, name="logout_user"),
]
