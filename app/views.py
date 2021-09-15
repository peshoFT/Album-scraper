from django.shortcuts import render
from django.http import FileResponse


def index(request):
    return render(request, "app/index.html", {})


def download(request, path):
    return FileResponse(open("media/stoichi.jpg", "rb"))


# spotdl songurl --output media/
