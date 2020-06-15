from django.shortcuts import render, redirect
from products.models import Product
from products.forms import ProductModelForm

# Create your views here.
# All views receive a request as parameter, and they must return a response

def list_products(request):
    product = Product.objects.all()

    context = {
        'products': product,
        'products_empty': []
    }

    return render(request, 'products/List.html', context=context)

def create_product(request):
    if request.method == 'POST':
        #salvar formulario
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/list')
    else:
        #get formulario
        form = ProductModelForm(request.GET) 
        
    context = {
        'form': form
    }

    return render (request, 'products/Create.html', context=context)

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('/products/list')

def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if (request.method == 'POST'):
        #salvar form
        form = ProductModelForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products/list')
    else:
        form = ProductModelForm(instance=product)

    context = {
        'form': form
    }

    return render(request, 'products/update.html', context=context)
