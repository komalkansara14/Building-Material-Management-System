from django.db import models

# Create your models here.
class UserRegistration(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cemail = models.EmailField()
    password = models.CharField(max_length=10)
    #cpassword = models.CharField(max_length=10)
    phone_no = models.IntegerField(unique=True)
    address = models.TextField(max_length=200)
    verify = models.BooleanField(default=False)
    role = models.CharField(max_length=100,default='user')
    
    def __str__(self):

        return self.name

class TransporterRegistration(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cemail = models.EmailField()
    password = models.CharField(max_length=10)
    #cpassword = models.CharField(max_length=10)
    phone_no = models.IntegerField(unique=True)
    vehicle_no = models.CharField(max_length=20, unique=True)
    address = models.TextField(max_length=200)
    verify = models.BooleanField(default=False)
    role = models.CharField(max_length=100,default='transporter')

    def __str__(self):

        return self.name


class GoDownStock(models.Model):
    cement_amount = models.IntegerField(default=0,blank=True)
    cement_price = models.IntegerField(default=0,blank=True)
    sand_amount = models.IntegerField(default=0,blank=True)
    sand_price = models.IntegerField(default=0,blank=True)
    brick_amount = models.IntegerField(default=0,blank=True)
    brick_price = models.IntegerField(default=0,blank=True)
    

    def __str__(self):
        return str(self.cement_amount) + ' ' +str(self.sand_amount) + ' ' + str(self.brick_amount)
    
class Price(models.Model):
    cprice = models.IntegerField()
    bprice = models.IntegerField()
    sprice = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=100,default='')
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.TextField(blank=True)
    status = models.CharField(max_length=20,default='pending')
    total_amount = models.IntegerField()

    def __str__(self):
        return self.user.name + ' ' + self.material_name + ' ' + str(self.quantity)
    

class Transaction(models.Model):
    
    made_by = models.ForeignKey(UserRegistration, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class ContactUs(models.Model):

    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return self.name 

class PaidOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    transporter =  models.ForeignKey(TransporterRegistration,on_delete=models.CASCADE, blank=True,null=True)
    pay_id = models.CharField(max_length=50,blank=True,null=True)
    remarks = models.TextField(blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.material_name

class CompletedDelivery(models.Model):
    
    delivered = models.ForeignKey(PaidOrder, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="Delivery remaining")

    def __str__(self):
        return self.delivered.transporter.name
    