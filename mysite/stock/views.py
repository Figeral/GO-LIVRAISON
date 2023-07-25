from django.shortcuts import render
from stock.models import Supplier,Category,Article

#showing all category  with a paginator to show to show more
def all_category(request):
    categories=Category.objects.all()
    articles=Article.objects.all()
    return render(request,'template/enfants/welcome.html',{
        'categories':categories,
        'articles':articles,
    })


#defining all article under a category
def all_article(request,cat_name):
    return

#detail on given article
def detail(request,article_id):
    return