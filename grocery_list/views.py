from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('grocery_list/index.html')
    context = {
        'item_list': item_list,
    }

    return HttpResponse(template.render(context, request))

    
def detail(request, item_id):
    response = "Viewing details about %s." 
    return HttpResponse(response % item_id)
