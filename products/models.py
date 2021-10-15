from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    tags = models.CharField(max_length=100)  # other Model name was not mentioned to which many to many relationship is to be create.
    Image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

