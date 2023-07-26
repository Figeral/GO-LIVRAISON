from django.db import models
from stock.models import Article
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    pw = models.CharField('mots de pass',max_length=50)
    pwc = models.CharField('confirmation',max_length=50)
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.BigIntegerField()

    

    class Meta:
        verbose_name = "costumer"
        verbose_name_plural = "customers"

    def __str__(self):
        return self.name

class Order(models.Model):
    command=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='customer_order',null=True)
    date = models.DateField(default=timezone.now)
    complete = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")

    def __str__(self):
        return str(self.id)
class ArticleOrder(models.Model):
    command=models.ForeignKey(Order,on_delete=models.SET_NULL,related_name='order_articleorder',null=True)
    article=models.ForeignKey(Article,on_delete=models.SET_NULL,related_name='article_articleorder',null=True)
    quantity = models.IntegerField()
    
    
    class Meta:
        verbose_name = ("Article_Order")
        verbose_name_plural = ("Article_Orders")

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='customer_sa',null=True)
    command=models.ForeignKey(Order,on_delete=models.SET_NULL,related_name='Order_sa',null=True)
    town = models.CharField(max_length=50)
    quater = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("shippingAddress")
        verbose_name_plural = ("shippingAddresses")

    def __str__(self):
        return self.quater





