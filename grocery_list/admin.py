from django.contrib import admin
from .models import Item
from .models import UserList

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_type', 'status')
    #pass
    #fields = ('name', 'item_type', 'status')

class UserListAdmin(admin.ModelAdmin):
    list_display = ('owner',)

admin.site.register(Item, ItemAdmin)
admin.site.register(UserList, UserListAdmin)

