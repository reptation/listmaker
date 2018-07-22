from django.db import models

   
class Item(models.Model):
    ITEM_TYPES = (
        ('produce', 'Fruits and Vegetables'),
        ('packaged_goods', 'Packaged Goods'),
        ('meat_and_fish', 'Meat and Fish'),
        ('bulk_goods', 'Bulk Goods'),
    ) 

    ITEM_STATUS = (
        ('good', 'good'),
        ('low', 'low'),
        ('out', 'out'),
    )

    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=30, choices=ITEM_TYPES)
    status = models.CharField(max_length=30, choices=ITEM_STATUS)

    def __str__(self):
        return self.name

