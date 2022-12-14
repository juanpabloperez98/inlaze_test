from django.urls import path
from users.views import Login, LogOut, RegisterUser

from .views import *

app_name = "users_app"

urlpatterns = [
    path("login", Login.as_view()),
    path("register_user", RegisterUser.as_view()),
    path("log_out", LogOut.as_view())
]
