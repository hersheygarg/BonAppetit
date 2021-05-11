from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 20, blank =True, null=True)
    
    def __str__(self):
        return self.name

class Dish(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, blank =True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    dis = models.TextField(null=True, blank =True)
    img = models.FileField(null=True, blank =True)
    img1 = models.FileField(null=True, blank =True)
    img2 = models.FileField(null=True, blank =True)
    price = models.IntegerField(null=True, blank =True)
    mrp = models.IntegerField(null=True, blank =True)
    avail = models.BooleanField(default=True, blank =True, null=True)
    
    def __str__(self):
        return self.title + '----' + self.cat.name
    
class Team(models.Model):
    img = models.FileField(null=True, blank =True)
    name = models.CharField(null=True, blank =True, max_length = 20)
    designation = models.CharField(null=True, blank =True, max_length = 20)
    fb = models.URLField(null=True, blank =True)
    twiter = models.URLField(null=True, blank =True)
    insta = models.URLField(null=True, blank =True)
    
    def __str__(self):
        return self.name