from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_type', 'status')
    #pass
    #fields = ('name', 'item_type', 'status')

admin.site.register(Item, ItemAdmin)
