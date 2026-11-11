from django.contrib import admin
from index.models import *
# Register your models here.





admin.site.site_header = "پنل مدیریت املاک"
admin.site.site_title = "مدیریت املاک"
admin.site.index_title = "به پنل مدیریت خوش آمدید"


class AdminListAds(admin.ModelAdmin):
    list_display = ['title','id','address','property_type','status','special_sale']
    list_filter = ['status','special_sale']
    search_fields = ['id','title']

admin.site.register(List_ads,AdminListAds)
admin.site.register(Property_Type_List)
admin.site.register(Neighborhoods)