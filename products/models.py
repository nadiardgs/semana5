from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return '{} - {}'.format(self.name, self.products.count())
        #{self.name} - {self.products.count()}'
    
    #this class indicates to Django admin how to create the plural of the base class name
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category, 
        on_delete=models.deletion.DO_NOTHING, 
        related_name='products'
    )

    def __str__(self):
        return self.name


