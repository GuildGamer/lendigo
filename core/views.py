from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Item
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers as sz

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

            data = serializer.data

            hid = data.get("id")
            by = data.get("by")
            kids = data.get("kids")
            score = data.get("score")
            time = data.get("time")
            type = data.get("type")
            deleted = data.get("deleted")
            dead = data.get("dead")  
            title = data.get("title")
            descendants = data.get("descendants")
            url = data.get("url")
            text = data.get("text")
            parts = data.get("parts")

            item = Item.objects.create (
                hid = hid,
                by = by,
                kids = kids,
                score = score,
                time = time,
                type = type,
                deleted = deleted,
                dead = dead,
                title = title,
                descendants = descendants,
                url = url,
                text = text,
                parts = parts,
            )

            item.save()

            serial = sz.ItemSerializer(data=item)
            serial.is_valid()
            return Response({"success":True, "data":serial.data}, status=status.HTTP_200_OK)
        else:
            return Response({"success":False, "error":serializer.errors, "data":None}, status=status.HTTP_400_BAD_REQUEST)
