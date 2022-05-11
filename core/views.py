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

    # def get_queryset(self):
    #     """
    #     Oviriding get_queryset method to populate the database if it is empty
    #     """
    #     items_qs = Item.objects.all()

        
    #         # populate(100, max_item)

    #     return self.queryset
        
    @action(
        methods=["POST"],
        detail=False,
        url_path="add",
        permission_classes=[AllowAny],
    )
    def add_item():
        pass


# update.delay()


# tl = Timeloop()

# TIMER LOGIC FOR UPDATING DATABASE EVERY 5 MINUTES
# WAIT_SECONDS = 300

# @tl.job(interval=timedelta(seconds=30))
# def update():
#     current_db_max = Item.objects.aggregate(Max('id'))
#     current_db_max_id = current_db_max["id__max"]

#     try:
#         response = requests.get(url=url)
#         max_id = response.json()

#     except requests.ConnectionError:
#         print("ERROR: COULDN'T GET MAX_ID")
#         pass
    
    # CALCULATES THE DIFFERENCE BETWEEN THE CURRENT MAX_ID AND THE LAST MAX_ID STORED IN DB
    # number = max_id - current_db_max_id 

    # populate(number, max_id)

    # threading.Timer(WAIT_SECONDS, update).start()

# CONFIRMS THAT DATABASE IS NOT EMPTY BEFORE IT CALLS PERIODICALLY
# items_qs = Item.objects.all()
# if items_qs:
#     tl.start(block=True)

    
