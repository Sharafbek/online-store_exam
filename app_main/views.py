from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, Category

class ProductsView(ListView):
    template_name = 'app_main/products.html'
    
    def get_queryset(self):
        return Product.objects.all
    
    context_object_name = 'products'


def category_page(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request=request,
                  template_name='app_main/categories.html',
                  context=context)

