# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import url

from models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    save_as = True  # 保存为新的
    save_as_continue = False  # 默认为True时， save_as 后留在编辑页， False时， save_as 后返回列表页
    list_display = ('name', 'price', 'source', 'picture')  # django admin 会默认将list_display的第一个参数作为跳转编辑页的选项
    search_fields = ('name',)
    # list_filter = ('price',)
    # list_editable = ('price',)  # 在列表页直接编辑 多条一起编辑一起保存
    # list_display_links = None
    # fields = ('name', 'price', 'source', 'picture')
    fieldsets = ((u"详情",
                  {"fields": ('name', 'price', 'source', 'picture'),
                   "description": u"测试说明"}
                  ),)