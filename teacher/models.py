from django.db import models


class Teacher(models.Model):
    tName = models.CharField(max_length=5, verbose_name="教师姓名")
    tPhone = models.CharField(max_length=11, verbose_name="联系电话")

    def __str__(self):
        return self.tName


