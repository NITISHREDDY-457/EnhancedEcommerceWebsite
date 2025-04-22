from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    
    

    # coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)
    # final_price = models.FloatField(null=True, blank=True)  # discounted price

    # def __str__(self):
    #     return f"Order #{self.id} by {self.customer}"
# class Coupon(models.Model):
#     code = models.CharField(max_length=20, unique=True)
#     discount = models.PositiveIntegerField(help_text="Discount percentage (e.g., 10 for 10%)")
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.code

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.FloatField(help_text="Enter percentage value (e.g. 10 for 10%)")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code



class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class SareeCustomizationFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"
