from django.shortcuts import render

from .models import Product, Category

def home_page(request):
    query = request.GET.get('q')
    search = request.GET.get('search', '')

    products = Product.objects.all()

    if query:
        products = Product.objects.filter(name__icontains=search)


    context={
        'products' : products,
        'search' : search,
    }

    return render(request=request,
                  template_name='index.html',
                  context = context)


def category_page(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request=request,
                  template_name='categories.html',
                  context=context)

