from django.contrib import admin
from django.urls import path, include
from Ledingo_challenge import urls
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("api/", include("core.urls", namespace="core")),
]
