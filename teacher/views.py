from django.shortcuts import render
from user import models
from .models import Teacher
from django.http import JsonResponse, HttpResponse


def t_show(request):
    """教师界面"""
    return render(request, "teacher/show.html")


def equipmentlist(request):
    """设备列表"""
    equipments = models.Equipment.objects.all()
    return render(request, "teacher/equipmentlist.html", {"equipments": equipments})


def kindjsj(request):
    """计算机类设备列表"""
    equipments = models.Equipment.objects.all().filter(eKind="计算机类")
    return render(request, "teacher/kindjsj.html", {"equipments": equipments})


def kindsw(request):
    """生物类设备列表"""
    equipments = models.Equipment.objects.all().filter(eKind="生物类")
    return render(request, "teacher/kindsw.html", {"equipments": equipments})


def kindhx(request):
    """化学类设备列表"""
    equipments = models.Equipment.objects.all().filter(eKind="化学类")
    return render(request, "teacher/kindhx.html", {"equipments": equipments})


def kindwl(request):
    """物理类设备列表"""
    equipments = models.Equipment.objects.all().filter(eKind="物理类")
    return render(request, "teacher/kindwl.html", {"equipments": equipments})


def kindjx(request):
    """机械类设备列表"""
    equipments = models.Equipment.objects.all().filter(eKind="机械类")
    return render(request, "teacher/kindjx.html", {"equipments": equipments})


def kindqt(request):
    """其它类设备列表"""
    equipments = models.Equipment.objects.all().filter(eKind="其它类")
    return render(request, "teacher/kindqt.html", {"equipments": equipments})


def stateable(request):
    """可借状态设备列表"""
    equipments = models.Equipment.objects.all().filter(eState="可借")
    return render(request, "teacher/stateable.html", {"equipments": equipments})


def stateunable(request):
    """借出状态设备列表"""
    equipments = models.Equipment.objects.all().filter(eState="借出")
    return render(request, "teacher/stateunable.html", {"equipments": equipments})


def edit(request):
    """编辑设备信息"""
    eid = request.GET['eid']
    equipment = models.Equipment.objects.get(id=int(eid))
    return render(request, "teacher/edit.html", {"equipment": equipment})


def update(request):
    """更新设备信息"""
    eid = request.GET["eid"]
    e = models.Equipment.objects.get(id=eid)
    e.eName = request.POST["eName"]
    e.eKind = request.POST["eKind"]
    e.eRoom = request.POST["eRoom"]
    t = Teacher.objects.get(tName=e.eTeacher.tName)
    t.tName = request.POST["tName"]
    t.tPhone = request.POST["tPhone"]
    try:
        e.save()
        t.save()
    except Exception:
        return JsonResponse({"code": 1})
    else:
        return JsonResponse({"code": 2})


def delete(request):
    """删除设备信息"""
    eid = request.GET["eid"]
    equipment = models.Equipment.objects.filter(id=eid)
    try:
        equipment.delete()
    except Exception:
        return HttpResponse("删除失败")
    else:
        return HttpResponse("删除成功")


def addequipment(request):
    """添加设备"""
    teachers = Teacher.objects.all()
    return render(request, "teacher/addequipment.html", {"teachers": teachers})


def save(request):
    """保存添加的内容"""
    eName = request.POST["eName"]
    eKind = request.POST["eKind"]
    eRoom = request.POST["eRoom"]
    etName = request.POST["tName"]
    teacher = Teacher.objects.get(tName=etName)
    try:
        models.Equipment.objects.create(eName=eName, eKind=eKind, eRoom=eRoom,
                                        eTeacher=teacher)
    except Exception:
        return JsonResponse({"code": 1})
    else:
        return JsonResponse({"code": 2})


def userlist(request):
    users = models.User.objects.all()
    return render(request, "teacher/userlist.html", {"users": users})


def deleteuser(request):
    """删除用户信息"""
    uid = request.GET["uid"]
    user = models.User.objects.filter(id=uid)
    try:
        user.delete()
    except Exception:
        return HttpResponse("删除失败")
    else:
        return HttpResponse("删除成功")


def applylist(request):
    """申请列表"""
    equipments = models.Equipment.objects.all().filter(eState="待确认")
    return render(request, "teacher/applylist.html", {"equipments": equipments})


def yes(request):
    """确认归还"""
    eid = request.GET["eid"]
    uid = request.GET["uid"]
    equipment = models.Equipment.objects.get(id=eid)
    user = models.User.objects.get(id=uid)
    apply = models.Applylist.objects.get(equipment=equipment)
    equipment.eStudent = None
    equipment.eState = "可借"
    user.useCount -= 1
    try:
        user.save()
        equipment.save()
        apply.delete()
    except Exception:
        return HttpResponse("确认失败！")
    else:
        return HttpResponse("确认成功！")
