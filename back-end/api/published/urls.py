from django.urls import path

from published.models import Published
from published.views import PublishedByUserSession

from .views import *

app_name = "published_app"

urlpatterns = [
    path("show_publisheds", PublishedByUserSession.as_view()),
]
