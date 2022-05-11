from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("items", views.ItemsViewSet, basename="items")

app_name = "core"

urlpatterns = router.urls