from django.db import models
from stock.models import *
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL,name='User_Customer',null=True)
    
    class Meta:
        verbose_name = "costumer"
        verbose_name_plural = "customers"

    def __str__(self):
        return self.user.first_name
#cart representation
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='customer_order',null=True)
    date = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")

    def __str__(self):
        return str(self.id)
    @property
    def grandtotal(self):
        cartitems=self.order_articleorder.all()
        total=sum([ArticleOrder.subtotal for item in cartitems])
        return total
    
    @property
    def cartquantity(self):
        cartitems=self.order_articleorder.all()
        total=sum([ArticleOrder.quantity for item in cartitems])
        return total
        
class ArticleOrder(models.Model):
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,related_name='order_articleorder',null=True)
    article=models.ForeignKey(Article,on_delete=models.SET_NULL,related_name='article_articleorder',null=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = ("Article_Order")
        verbose_name_plural = ("Article_Orders")
    @property
    def subtotal(self):
        total=self.quantity*self.article.price
        return total
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='customer_sa',null=True)
    command=models.ForeignKey(Order,on_delete=models.SET_NULL,related_name='Order_sa',null=True)
    tel = models.BigIntegerField(null=False,default=False)
    town = models.CharField(max_length=50)
    quater = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("shippingAddress")
        verbose_name_plural = ("shippingAddresses")

    def __str__(self):
        return self.quater





