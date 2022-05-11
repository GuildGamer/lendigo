from urllib import response
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Item
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers as sz
import requests
from decouple import config
import time, threading
from django.db.models import Max
from timeloop import Timeloop
from datetime import timedelta

from .tasks import update, populate, url

class ItemsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = sz.ItemSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['type']
    queryset = Item.objects.all()
        
    @action(
        methods=["POST"],
        detail=False,
        url_path="add",
        permission_classes=[AllowAny],
    )
    def add_item(self, request):
        serializer = sz.ItemSerializer(data=request.data)

        if serializer.is_valid():
            item = serializer.save()
            return Response({"success":True, "data":sz.ItemSerializer(data=item).data}, status=status.HTTP_200_OK)
        else:
            return Response({"success":False, "error":serializer.errors, "data":None}, status=status.HTTP_400_BAD_REQUEST)
