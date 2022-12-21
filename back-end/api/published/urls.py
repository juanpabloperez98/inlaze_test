from django.urls import path
from published.models import Published
from published.views import PublishedAPI, PublishedByUserSession

from .views import *

app_name = "published_app"

urlpatterns = [
    path("publisheds", PublishedByUserSession.as_view()),
    path("all/publisheds", PublishedAPI.as_view()),
]
