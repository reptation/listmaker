from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from django_tables2 import RequestConfig
 
from .models import Item
from .tables import ItemTable

#def index(request):
#    item_list = Item.objects.all()
#    pg = Item.objects.filter(item_type='packaged_goods')
#    fv = Item.objects.filter(item_type='produce')
#    mf = Item.objects.filter(item_type='meat_and_fish')
#    bg = Item.objects.filter(item_type='bulk_goods')
#    context = {
#        'item_list': item_list,
#        'packaged_goods': pg,
#        'fruit_and_vegetables': fv,
#        'meat_and_fish': mf,
#        'bulk_goods': bg
#    }
#    return render(request, 'grocery_list/index.html', context)

def index(request):
    table = ItemTable(Item.objects.all())
    return render(request, 'grocery_list/index.html', { 'table': table })

    
def detail(request, item_id):
    response = "Viewing details about %s." 
    return HttpResponse(response % item_id)


def need(request):
    needed_item_list = Item.objects.exclude(status='good')
    context = {
        'needed_item_list': needed_item_list,
    }
    return render(request, 'grocery_list/get.html', context)
