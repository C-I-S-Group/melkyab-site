from django.db import models

# Create your models here.

class List_ads(models.Model):
    property_type_list = [('apartment','آپارتمان'),('vila','ویلا'),('land','زمین')]
    title = models.CharField(max_length=1000)
    price = models.PositiveBigIntegerField()
    descriptions = models.TextField()
    area = models.PositiveIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    # img = models.ImageField()
    address = models.CharField(max_length=10000)
    property_type = models.CharField(choices=property_type_list,max_length=1000)
    status = models.BooleanField()

    def __str__(self):
        return self.title
    
    