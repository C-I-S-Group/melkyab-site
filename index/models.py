from django.db import models

# Create your models here.

class List_ads(models.Model):
    property_type_list = [('apartment','آپارتمان'),('vila','ویلا'),('land','زمین')]
    title = models.CharField(max_length=1000,verbose_name="عنوان آگهی")
    price = models.PositiveBigIntegerField(verbose_name="قیمت")
    descriptions = models.TextField(verbose_name="توضیحات بیشتر")
    area = models.PositiveIntegerField(verbose_name="متراژ")
    bedrooms = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق ها")
    # img = models.ImageField()
    address = models.CharField(max_length=10000,verbose_name="آدرس")
    property_type = models.CharField(choices=property_type_list,max_length=1000,verbose_name="نوع آکهی")
    status = models.BooleanField(verbose_name="وضعیت آگهی",default=0)
    class Meta():
        verbose_name = "آگهی"
        verbose_name_plural = "آگهی ها"

    def __str__(self):
        return self.title
    
    