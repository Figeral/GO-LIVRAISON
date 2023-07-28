from django.shortcuts import render,get_object_or_404
from stock.models import Supplier,Category,Article

#showing all category  with a paginator to show to show more
def all_category(request):
    categories=Category.objects.values('reference').distinct()
    articles=Article.objects.order_by("name")
    return render(request,'template/enfants/welcome.html',{
        'categories':categories,
        'articles':articles,
    })


#defining all article under a category
def see_more(request,cat_ref):
    host=Category.objects.filter(reference=cat_ref).first()
    articles=host.category_article.filter(category=host.id)
    return render(request,'template/enfants/article.html',{'articles':articles})

#detail on given article
def detail(request,article_id):
    return