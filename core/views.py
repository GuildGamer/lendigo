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

url = config("HACKER_NEWS_MAX_ID")

class ItemsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = sz.ItemSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['type']
    queryset = Item.objects.all()

    def populate(self, number: int, max: int):
        for i in range(number):
            item_id = max - i
            response = requests.get(url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(item_id))
            item = response.json()
            serializer = self.serializer_class(data=item)
            if serializer.is_valid():
                try:
                    item = serializer.save()
                    print("CREATED SUCCESSFULLY")
                except Exception as e:
                    print(f"ERROR {e}")
            else:
                print(serializer.errors)

            

    def get_queryset(self):
        items_qs = Item.objects.all()
        if not items_qs:
            # add error handling
            response = requests.get(url=url)
            max_item = response.json()
            print (max_item)
            self.populate(100, max_item)
        return self.queryset
        
    @action(
        methods=["POST"],
        detail=False,
        url_path="add",
        permission_classes=[AllowAny],
    )
    def add_item():
        pass
