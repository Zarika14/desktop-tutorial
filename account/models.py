from django.db import models
from django.contrib.auth.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User, related_name='products')
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.name
    
    


