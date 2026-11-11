from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Neighborhoods(models.Model):
    neighborhood = models.CharField(verbose_name="محله", max_length=50)
    class Meta():
        verbose_name = "محله"
        verbose_name_plural = "محله ها"

    def __str__(self):
        return self.neighborhood



class Property_Type_List(models.Model):
    property_type_list = models.CharField(max_length=5000,verbose_name="نوع آگهی")


    class Meta():
        verbose_name = "دسته بندی نوع آگهی"
        verbose_name_plural = "نوع آگهی ها"

    def __str__(self):
        return self.property_type_list

class List_ads(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='کد آگهی')
    title = models.CharField(max_length=1000,verbose_name="عنوان آگهی")
    price = models.PositiveBigIntegerField(verbose_name="قیمت")
    area = models.PositiveIntegerField(verbose_name="متراژ")
    # img = models.ImageField()
    address = models.ForeignKey(Neighborhoods,verbose_name="آدرس",on_delete=models.PROTECT)
    full_address = models.TextField(verbose_name="آدرس کامل")
    property_type = models.ForeignKey(Property_Type_List,on_delete=models.PROTECT,verbose_name="نوع آگهی")
    year_of_construction = models.PositiveIntegerField(verbose_name="سال ساخت")
    all_floors = models.PositiveSmallIntegerField(verbose_name="کل طبقه های ساختمان")
    the_floor_of = models.PositiveSmallIntegerField(verbose_name="طبقه ی")
    bedrooms = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق ها")
    has_balcony = models.BooleanField(verbose_name="تراس")
    has_parking = models.BooleanField(verbose_name="پارکینگ")
    has_storage_room = models.BooleanField(verbose_name="انباری")
    elevator = models.BooleanField(verbose_name="آسانسور")
    descriptions = models.TextField(verbose_name="توضیحات بیشتر")
    status = models.BooleanField(verbose_name="وضعیت آگهی",default=0)
    special_sale = models.BooleanField(verbose_name="فروش ویژه")
    class Meta():
        verbose_name = "آگهی"
        verbose_name_plural = "آگهی ها"

    def __str__(self):

        return self.title
    
    def clean(self):
        if self.the_floor_of > self.all_floors:
            raise ValidationError({
                'the_floor_of': 'باید کوچک تر مساوی از کل طبقه ها باشد .'
            })

