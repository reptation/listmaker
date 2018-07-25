from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

from .models import Item

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'grocery_list/index.html', context)

    
def detail(request, item_id):
    response = "Viewing details about %s." 
    return HttpResponse(response % item_id)


def need(request):
    needed_item_list = Item.objects.exclude(status='good')
    context = {
        'needed_item_list': needed_item_list,
    }
    return render(request, 'grocery_list/get.html', context)
