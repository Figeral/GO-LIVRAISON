from django.urls import path
from . import views

app_name='stock'
urlpatterns = [
    path('',views.all_category,name='acceuil'),
    path('Category/<slug:cat_ref>/',views.see_more,name='see_more'),
    path('search/',views.search_item,name='search_item'),
]
