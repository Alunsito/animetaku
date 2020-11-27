from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Este es la página de inicio de animetaku")

def anime_info(request, anime_id):
    return HttpResponse("You're looking at anime %s." % anime_id)

def anime_review(request, review_id):
    return HttpResponse("You're looking at review %s." % anime_id)