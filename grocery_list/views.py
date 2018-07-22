from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to your Grocery List")

    
def detail(request, item_id):
    response = "Viewing details about %s." 
    return HttpResponse(response % item_id)
