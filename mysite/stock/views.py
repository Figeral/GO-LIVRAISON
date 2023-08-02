from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from stock.models import Supplier,Category,Article
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

#showing all category  with a paginator to show to show more
def all_category(request):
    categories=Category.objects.all()
    articles=Article.objects.filter(status='ua')

    return render(request,'template/enfants/welcome.html',{
        'categories':categories,
        'articles':articles,
        
    })


#defining all article under a category
def see_more(request,cat_ref):
    category=Category.objects.get(slug=cat_ref)
    articles=category.category_article.filter(category=category)
    return render(request,'template/enfants/more_article.html',{'articles':articles,
                                                                'category':category})

#detail on given article
# def detail(request,article_id):
#     return

def search_item(request):
    if request.method == "GET":
        querry=request.GET.get('query')
        articles=Article.objects.filter(name__icontains= querry)
        return render(request,'template/enfants/search.html',{
        'articles':articles,
        })
        
    