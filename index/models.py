from django.db import models

# Create your models here.

class Property_Type_List(models.Model):
    property_type_list = models.CharField(max_length=5000,verbose_name="نوع آگهی")


    class Meta():
        verbose_name = "دسته بندی نوع آگهی"
        verbose_name_plural = "نوع آگهی ها"

    def __str__(self):
        return self.property_type_list

class List_ads(models.Model):
    title = models.CharField(max_length=1000,verbose_name="عنوان آگهی")
    price = models.PositiveBigIntegerField(verbose_name="قیمت")
    area = models.PositiveIntegerField(verbose_name="متراژ")
    # img = models.ImageField()
    address = models.CharField(max_length=10000,verbose_name="آدرس")
    property_type = models.ForeignKey(Property_Type_List,on_delete=models.PROTECT,verbose_name="نوع آگهی")
    bedrooms = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق ها")
    has_balcony = models.BooleanField(verbose_name="بالکن")
    has_parking = models.BooleanField(verbose_name="پارکینگ")
    has_storage_room = models.BooleanField(verbose_name="انباری")
    descriptions = models.TextField(verbose_name="توضیحات بیشتر")
    status = models.BooleanField(verbose_name="وضعیت آگهی",default=0)
    special_sale = models.BooleanField(verbose_name="فروش ویژه")
    class Meta():
        verbose_name = "آگهی"
        verbose_name_plural = "آگهی ها"

    def __str__(self):
        return self.title

