from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse(f"Hello, world. You're at the Lendigo News API index. {datetime.now()}")
