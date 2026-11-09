from django.contrib import admin
from index.models import *
# Register your models here.





admin.site.site_header = "پنل مدیریت املاک"
admin.site.site_title = "مدیریت املاک"
admin.site.index_title = "به پنل مدیریت خوش آمدید"


admin.site.register(List_ads)