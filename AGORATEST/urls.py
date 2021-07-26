"""AGORATEST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import  settings
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from agora.views import Agora
from App.models import Channel

channel=""
app_id="replace_with_app_id"
if Channel.objects.filter(app_id=app_id):
    channel=Channel.objects.filter(app_id=app_id).last().channel


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("App.urls")),
    path('agora/',Agora.as_view(
    app_id=app_id,
    channel=channel)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
