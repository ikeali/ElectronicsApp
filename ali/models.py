from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AppInfo(models.Model):
    appname = models.CharField(max_length=50)
    logo = models.ImageField(upload_to = 'logo')
    banner = models.ImageField(upload_to='banner')
    carousel1 = models.ImageField(upload_to='carousel1')
    carousel2 = models.ImageField(upload_to='carousel2')
    carousel3 = models.ImageField(upload_to='carousel3')

    def __str__(self):
        return self.appname
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    cating = models.ImageField(upload_to='cating')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model): 
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='product')
    price = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=50, blank=True, null=True)
    popular = models.BooleanField(default=False)
    featured = models.BooleanField(default = False)
    upload = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message =models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Customer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        first_name =models.CharField(max_length=100)       
        last_name =models.CharField(max_length=100)       
        phone =models.CharField(max_length=20)       
        address =models.CharField(max_length=100)       
        email =models.EmailField(max_length=104)       
        pix =models.ImageField(upload_to='profilepix')
        joined = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.user.username

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity =models.IntegerField()
    amount = models.CharField(max_length=50)
    paid = models.BooleanField()

    def __str(self):
        return self.user.username   

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)         
    last_name = models.CharField(max_length=50)         
    phone = models.CharField(max_length=50)         
    address = models.TextField()
    amount = models.IntegerField()
    paid = models.BooleanField()
    pay_code = models.CharField(max_length=50)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username          



        
    
  