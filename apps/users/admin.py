from django.contrib import admin
from .models import UserInfo
import xadmin
# Register your models here.

class UserInfoAdmin(object):
    list_display=('name','email','mobile')
    show_detail_fields=["name"]
    list_bookmarks = [{
        "title": "存在邮箱",
        "query": {"email__contains": '@'},
        "order": ("-name",),
        "cols": ('name', 'email', 'mobile'),
    }]
xadmin.site.register(UserInfo,UserInfoAdmin)
