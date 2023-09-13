from django.db import models

# Create your models here.

class Item(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, default='xyz')
    item_name = models.CharField(max_length=  50)
    Item_desc = models.CharField(max_length =500,
        default = '''Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ipsum exercitationem deserunt quidem vel magni saepe voluptates minima ab ex! Quam, quae atque nulla accusamus cum illum. Aliquam aspernatur modi ipsum?''' 
        )
    item_price = models.IntegerField()
    item_img = models.CharField(
        max_length=500,
        default="https://static.vecteezy.com/system/resources/previews/003/170/825/original/isolated-food-plate-fork-and-spoon-design-free-vector.jpg"
        )

    def __str__(self):
        return self.item_name