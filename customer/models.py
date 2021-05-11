from django.db import models
from django.contrib.auth.models import User
from management.models import Dish

class Add_to_cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True, default=1)
    confirmation = models.BooleanField(blank=True, null=True, default=False)
    
    def __str__(self):
        return self.dish.title
    
    
class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    mob = models.IntegerField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length = 20)
    guests = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    confirm = models.BooleanField(blank=True, null=True, default=False)
    
    def __str__(self):
        return self.name + '---' + str(self.date) + '---' + str(self.time)
    
    