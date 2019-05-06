from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=100000, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('catalog.ProductCategory')
    image = models.ImageField(upload_to='img')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Opened at')
    closed_at = models.DateTimeField(verbose_name='Closed at', blank=True, null=True)
    is_closed = models.BooleanField(default=True, verbose_name='Is closed')
    is_processed = models.BooleanField(default=True, verbose_name=' Is processed')
    phone = models.CharField(max_length=32, null=True)
