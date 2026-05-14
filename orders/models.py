from django.db import models

class OrderStatus(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.ForeignKey(OrderStatus,ondelete=models.SET_NULL,null=True)
    def __str__(self):
        return self.customer_name
class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    discount_percentage=models.DecimalField(max_digits=5,decimal_places=2)
    is_active=BooleanField(default=True)
    vaild_form=models.DateFiled()
    vaild_until=models.DateFiled()
    def __str__(self):
        return self.code
