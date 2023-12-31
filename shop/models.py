from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    has_parent = models.BooleanField(default=False)
    
        
    def __str__(self):
        return self.name
 
class ChildMenu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    
    def get_all_menus_by_parentid(id):
        return ChildMenu.objects.filter(parent=id)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to="uploads/products/")
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products()
    
    def __str__(self):
        return self.name

