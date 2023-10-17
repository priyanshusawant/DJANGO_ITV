from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        default='1'
    )
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
    

class HISTORY(models.Model):

    user_name = models.CharField(max_length=100)
    prod_ref = models.IntegerField(default=100)
    item_name = models.CharField(max_length=200)
    op_type = models.CharField(max_length=100)

    def __str__(self):
        return str(
            (
                self.prod_ref,
                self.user_name,
                self.item_name,
                self.op_type
            )
        )