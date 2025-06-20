from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register, logout

urlpatterns = [
    path("signup", register, name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
