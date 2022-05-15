from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.db.models import Max
from .models import Item
import requests
from decouple import config
from . import serializers as sz

url = config("HACKER_NEWS_MAX_ID")
items_qs = Item.objects.all()

# REQUESTED ITEM CELERY SHARED TASK
@shared_task(name = "request_item")
def request_item(item_id: int):
    """
    gets an item from hacker news. params: item_id
    """
    response = requests.get(url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(item_id))

    item = response.json()
    serializer = sz.ItemSerializer(data=item)

    if serializer.is_valid():
        try:
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

            # item = serializer.save()
            print("CREATED SUCCESSFULLY")

        except Exception as e:
            print(f"ERROR {e}")

    else:
        print(serializer.errors)

def populate(number: int, max: int) -> bool:
    """
    Populates database with items based on the param: number
    """
    for i in range(number):
        item_id = max - i

        # ASYNCHRONOUSLY GET ITEMS OF COUNT "number"
        request_item.delay(item_id)

        
    return True


def init_populate() -> bool:

    """
    function for initial population of database
    """

    print("INITIAL 100")
    if not items_qs:
        # add error handling
        try:
            response = requests.get(url=url)

        except requests.ConnectionError:
            print("THERE WAS AN ISSUE POPULATING THE DB. COULDN'T GET MAX_ID")
            return False
        
        max_item = response.json()
        print (max_item)
        is_populated = populate(100, max_item)

        return is_populated

@shared_task(name = "update")
def update() -> bool:

    """
    UPDATED THE DATABASE BY POPULATING IT WITH THE MOST RECENT ITEMS
    """

    is_initialised = init_populate()

    if is_initialised == True:

        current_db_max = Item.objects.aggregate(Max('hid'))
        current_db_max_id = current_db_max["hid__max"]

        try:
            response = requests.get(url=url)
            max_id = response.json()

        except requests.ConnectionError:
            print("ERROR: COULDN'T GET MAX_ID")
            return False
        
        # CALCULATES THE DIFFERENCE BETWEEN THE CURRENT MAX_ID AND THE LAST MAX_ID STORED IN DB
        number = max_id - current_db_max_id 

        if len(items_qs) >= 100:
            print("5 MINUTE UPDATE")
            populate(number, max_id)

        else:
            print("NOT DONE WITH INITIAL 100")
            return False

        return True
# CONFIRMS THAT DATABASE IS NOT EMPTY BEFORE IT CALLS PERIODICALLY