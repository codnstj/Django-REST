from django.db import models

class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)

class Menu(models.Model):
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateField('date ordered')
    estimated_time = models.IntegerField(default=-1)
    deliver_finish = models.BooleanField(default=0)
    address = models.CharField(max_length=40)

class Order_food(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
