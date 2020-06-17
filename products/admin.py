from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from products.models import Product, Category, Order
# Register your models here.


class CategoryModelAdmin(admin.ModelAdmin):
    def products(self, obj):
        #'/admin/APP-NAME_MODEL_NAME_changelist'
        href = reverse('admin:products_product_changelist') + f'?category={obj.pk}'
        return format_html (f'<a href="{href}">{ obj.products.count() }</a>')
    
    products.short_description = 'Produtos da categoria'
    list_display = ('name', 'description', 'products')

class ProductModelAdmin(admin.ModelAdmin):
    def queryset(self, request, queryset):
        category = request.GET.get('category')
        if category:
            return queryset.filter(category__pk=category)
        else:
            return queryset
    
    def link_category(self, obj):
        href = reverse('admin:products_category_change', args=(obj.category.pk,))
        return format_html(f'<a href="{href}">{obj.category.name}</a>')

    link_category.short_description = 'Categoria'

    def formatted_price(self, obj):
        return f'R$ {obj.price}'

    list_display = ('name', 'description', 'formatted_price', 'link_category')

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Order)
