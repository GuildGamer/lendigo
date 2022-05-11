from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    # return HttpResponse(f"Hello, world. You're at the Lendigo News API index. {datetime.now()}")

    return render(request, 'index.html', {})

def search_items(request):
    return render(request, 'search_items.html', {})


