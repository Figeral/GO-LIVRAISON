from django.urls import path
from . import views
import stock


app_name='livraison'
urlpatterns = [
    path('login/',views.log_in,name='log_in'),
    path('signin/',views.signin,name='signin'),
    path('',views.log_out,name='log_out'),
    path('',views.all_category,name='all_category')
]
