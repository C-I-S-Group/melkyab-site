from django.contrib import admin
from index.models import *
# Register your models here.


admin.site.site_header = "پنل مدیریت املاک"
admin.site.site_title = "مدیریت املاک"
admin.site.index_title = "به پنل مدیریت خوش آمدید"

class PropertyImageInline(admin.TabularInline):
    model = Property_Image
    extra = 3
    max_num = 10
    min_num = 1
    verbose_name = 'تصویر آگهی'
    verbose_name_plural = 'تصاویر آگهی'

class AdminListAds(admin.ModelAdmin):
    list_display = ['title','id','address','property_type','status','special_sale']
    list_filter = ['status','special_sale']
    search_fields = ['id','title']
    inlines = [PropertyImageInline]


class AdminConntact(admin.ModelAdmin):
    list_display = ['username','email','phone','subject','message']
    

admin.site.register(List_ads,AdminListAds)
admin.site.register(Property_Type_List)
admin.site.register(Neighborhoods)
admin.site.register(Conntact,AdminConntact)