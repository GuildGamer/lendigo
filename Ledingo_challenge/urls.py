from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("search-items/", search_items, name = 'search-items'),
    path("admin/", admin.site.urls),
    path("api/", include("core.urls", namespace="core")),
]

