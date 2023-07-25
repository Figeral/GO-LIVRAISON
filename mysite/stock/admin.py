from django.contrib import admin
from stock.models import Article,Category,Supplier

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
     list_display=['name','marque','color','category','number','price','added','status']
     search_fields=['name','marque','color','status','added']
     raw_id_fields=['category',]
     date_hierarchy='added'
     
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display=['reference','quantity','supplier']
     search_fields=['reference',]
     raw_id_fields=['supplier']
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
     list_display=['name','surname','store','location','telephone']
     search_fields=['name','surname','store','location']
