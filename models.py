from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50, default='')
    number_click = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(default=0)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(default='')
    number_click = models.IntegerField(default=0, blank=True)
    gender = models.CharField(max_length=20, default='Male')

    def __str__(self):
        return self.name

class Orders_male(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, blank=True)
    gift = models.CharField(max_length=50, default='')
    # def __str__(self):
    #     return self.order


class RegisterUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=12, default='')
    surname = models.CharField(max_length=12, default='')
    birthday = models.CharField(max_length=50, default='')
    adress = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    confirmpassword = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name + self.surname

class Unique_ProductMale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)

class P_M_images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
class Product_female(models.Model):
    name = models.CharField(max_length=50, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(default=0)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(default='')
    number_click = models.IntegerField(default=0, blank=True)
    gender = models.CharField(max_length=20, default='Female')

    def __str__(self):
        return self.name

class Orders_female(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Product_female, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, blank=True)
    gift = models.CharField(max_length=50, default='')

class P_F_images(models.Model):
    product = models.ForeignKey(Product_female, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
class Unique_ProductFemale(models.Model):
    product= models.ForeignKey(Product_female, on_delete=models.CASCADE, null=True, blank=True)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
class Footer(models.Model):
    name = models.CharField(max_length=50, default='')
    email1 = models.CharField(max_length=100, default='')
    email2 = models.CharField(max_length=100, default='')
    instagram = models.CharField(max_length=100, default='')
    number = models.CharField(max_length=100, default='')
    copyright = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=12, default='')
    surname = models.CharField(max_length=12, default='')
    email = models.EmailField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='')
    Comment = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.name + self.surname

class Subscribe(models.Model):
    email = models.EmailField(max_length=50, default='')

    def __str__(self):
        return self.email

class Payment(models.Model):
    fullname = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=50, default='')
    creditcard = models.CharField(max_length=20, default='')
    exp = models.CharField(max_length=5, default='')
    cvc = models.CharField(max_length=3, default='')

    def __str__(self):
        return self.fullname