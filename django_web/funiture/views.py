from django.shortcuts import render
from .models import Product, Category

def home(request):
    return render(request, 'base.html')

def allDesign(request):
    
    category = request.GET.get('category')
    if category == None:
        product = Product.objects.all().order_by('-id')
        categories = Category.objects.all()
        context = {
            'designs': product,
            'categories': categories
            }
        
        return render(request, 'allDesign.html', context)
    else:
        product = Product.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {
        'designs':product,
        'categories': categories
    }
    return render(request, 'category.html', context)
    