from django.contrib import admin
from stock.models import Article,Category,Supplier

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
     list_display=['name','marque','color','category','number','price','added','status']
     search_fields=['name','marque','color','status','added']
     date_hierarchy='added'
     
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display=['reference','slug','added','status']
     prepopulated_fields={'slug':('reference',)}
     search_fields=['reference','added','status']
    
     
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
     list_display=['name','store','location','telephone',]
     search_fields=['name','store','location',]
   