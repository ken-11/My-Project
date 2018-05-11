from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
  # 1.增加右侧过滤器
  list_filter = ['goodsType']
  # 2. 增加顶层搜索字段
  search_fields = ['title']


class UsersAdmin(admin.ModelAdmin):
  search_fields = ['uphone', 'uname', 'uemail']


# Register your models here.

admin.site.register(Users, UsersAdmin)
admin.site.register(GoodsType)
admin.site.register(Goods, GoodsAdmin)
