from django.db import models

# Create your models here.
class Customer(models.Model):
    customerid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Orders(models.Model):
    orderid=models.IntegerField(primary_key=True)
    customerid=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Orderdetails(models.Model):
    orderid=models.ForeignKey(Orders,on_delete=models.CASCADE)
    
    no_of_orders=models.IntegerField(default=1)
    cost=models.IntegerField()
   