from django.contrib import admin
from livraison.models import User,Customer,Order,ArticleOrder,ShippingAddress

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ArticleOrder)
admin.site.register(ShippingAddress)