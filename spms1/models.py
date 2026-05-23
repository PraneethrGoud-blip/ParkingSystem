from django.db import models
class login (models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    mobile=models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    parking_area_number=models.IntegerField()
    vehicle_type=models.CharField(max_length=100)
    vehicle_limit=models.IntegerField()
    parking_charge=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.vehicle_type
   
 
class Vehicle(models.Model):
    STATUS_CHOICES = (
        ('Parked', 'Parked'),
        ('Leaved', 'Leaved'),
    )
    PAYMENT_CHOICES = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    )
    vehicle_number=models.CharField(max_length=50)
    vehicle_type=models.ForeignKey(Category, on_delete=models.CASCADE)
    area_number=models.IntegerField()
    charges= models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    arrival_time=models.DateTimeField(auto_now_add=True)
    departure_time=models.DateTimeField(null=True,blank=True)
    parking_status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Parked')
    payment_status=models.CharField(max_length=20,choices=PAYMENT_CHOICES,default='Pending')
    wrong_parking=models.BooleanField(default=False)
    def __str__(self):
        return self.vehicle_number
 