from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=  50)
    Item_desc = models.CharField(max_length = 300)
    item_price = models.IntegerField()
    item_img = models.CharField(
        max_length=500,
        default="https://static.vecteezy.com/system/resources/previews/003/170/825/original/isolated-food-plate-fork-and-spoon-design-free-vector.jpg"
        )

    def __str__(self):
        return self.item_name