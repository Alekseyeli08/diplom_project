from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    ProfileView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserUpdateView,
)

app_name = UsersConfig.name


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("users/<int:pk>", UserDetailView.as_view(), name="user_detail"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path("", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
