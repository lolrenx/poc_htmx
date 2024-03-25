import niquests as re

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    url = "https://pokeapi.co/api/v2/pokemon/1/"
    data = re.get(url).json()
    context = {"data": data}
    return render(request,"core/index.html", context=context)
