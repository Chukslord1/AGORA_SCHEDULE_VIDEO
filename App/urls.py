from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = "APP"


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("schedule", views.schedule, name="schedule"),
    path("success/", views.success, name="success"),

]
