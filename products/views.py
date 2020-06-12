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