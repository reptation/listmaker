from django.forms import ModelForm
from .models import Item, UserList

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'status']


class UserListForm(ModelForm):
    class Meta:
        model = UserList
        fields = ['owner', 'items']


