from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    selling_no = models.IntegerField(default=0)
    about = models.TextField()
    model_or_brand = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    pan_number = models.CharField(max_length=10, unique=True)
    products = models.ManyToManyField(Product, related_name='customers')

    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.name} - {self.product.name} on {self.date_time.strftime("%Y-%m-%d %H:%M:%S")}'