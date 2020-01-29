from django.conf.urls import url
from . import views


urlpatterns = [
    url("", views.authors, name="authors"),
]
