from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader

from .models import Item
from .forms import NameForm
from .list_form import UserListForm

def index(request):
    item_list = Item.objects.all()
    produce_items = Item.objects.filter(item_type="produce")
    meat_items = Item.objects.filter(item_type="meat_and_fish")
    p_goods = Item.objects.filter(item_type="packaged_goods")
    bulk = Item.objects.filter(item_type="bulk_goods")
    item_types = Item.ITEM_TYPES
    item_types_hr = [x[1] for x in Item.ITEM_TYPES]
    item_status_hr = [x[1] for x in Item.ITEM_STATUS]
    context = {
        'item_list': item_list,
        'item_desc': item_types_hr,
        'bulk': bulk,
        'p_goods': p_goods,
        'meat_items': meat_items,
        'produce_items': produce_items,
        'status_types': item_status_hr,
        'item_types': item_types_hr
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

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'grocery_list/name.html', {'form': form})


def get_list(request):
    if request.method == 'POST':
        form = UserListForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = UserListForm()
    
    return render(request, 'grocery_list/list.html', {'form': form})

def thanks(request):
    response = "Thanks for keeping things updated"
    return HttpResponse(response)

    
