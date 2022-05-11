from django import conf
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import requests
from decouple import config

BASE_URL = config("BASE_URL")

def index(request):
    # return HttpResponse(f"Hello, world. You're at the Lendigo News API index. {datetime.now()}")

    return render(request, 'index.html', {})

def search_items(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        response = requests.get(f"{BASE_URL}/api/items?type={searched}")
        items = response.json()

        return render(request, 'search_items.html', {'searched':searched, 'items':items})
    else:
        return render(request, 'search_items.html', {})
