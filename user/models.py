from django.db import models
from teacher import models as T


class User(models.Model):
    userName = models.CharField(max_length=11, verbose_name='姓名')
    userNum = models.CharField(max_length=15, verbose_name='学号')
    userPhone = models.CharField(max_length=11, verbose_name='联系方式')
    userPwd = models.CharField(max_length=78, verbose_name='密码')
    useCount = models.IntegerField(default=0, verbose_name='已借数')

    def __str__(self):
        return "姓名：%s  学号：%s" % (self.userName, self.userNum)


class Equipment(models.Model):
    KIND_CHOICES = (
                    ("计算机类", "计算机类"),
                    ("机械类", "机械类"),
                    ("物理类", "物理类"),
                    ("化学类", "化学类"),
                    ("生物类", "生物类"),
                    ("其它类", "其它类"),
                    )
    eKind = models.CharField(max_length=10, verbose_name="设备类型", choices=KIND_CHOICES, default="请选择设备类型")
    eName = models.CharField(max_length=10, verbose_name="设备名称")
    eRoom = models.CharField(max_length=10, verbose_name="设备所在教室")
    eState = models.CharField(max_length=3, verbose_name="状态", choices=(('可借', '可借'), ('借出', '借出')), default="可借")
    eTeacher = models.ForeignKey(T.Teacher, on_delete=models.CASCADE, verbose_name="负责教师")
    eStudent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="借用学生", null=True, blank=True)

    def __str__(self):
        return self.eName


class Applylist(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="归还学生")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="归还设备")
