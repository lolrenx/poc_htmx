import niquests as re

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    url = "https://pokeapi.co/api/v2/pokemon/1/"
    data = []
    with re.Session(multiplexed=True) as s:
        for i in range(1, 150):
            url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
            r = s.get(url)
            data.append(r.json())

    context = {"data": data}
    return render(request,"core/index.html", context=context)
