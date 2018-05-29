# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestModel.models import Test, Tag, Contact

# Register your models here.

admin.site.register(Test)


# 注册多个模型来显示
admin.site.register(Tag)
admin.site.register(Contact)

# 上述也可以写在一个list里
admin.site.register([Test, Tag, Contact])

# 管理界面的显示格式
class ContactAdmin(admin.ModelAdmin):
    fields = ['name', 'email'] # fields定义了要显示的字段

admin.site.register(Contact, ContactAdmin) # 将二者一起注册
admin.site.register([Tag, Test])


# 让输入栏分块

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS 让下列字段隐藏
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])


# Contact是Tag的外部键，在默认界面内，二者分开无法显示从属关系
# 可以使用内敛inline让Tag附加在Contact的编辑页面上显示

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email', 'sex', 'adress'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])

# search_fields可以增加搜索栏
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email')
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
