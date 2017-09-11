from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=20,default="",verbose_name="负责人")
    email=models.EmailField(null=True,blank=True,verbose_name="邮箱")
    mobile=models.BigIntegerField(verbose_name="电话")
    class Meta:
        db_table="user_info"
        verbose_name="用户表"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name