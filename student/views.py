from django.shortcuts import render
from user import models
from django.http import HttpResponse


def s_show(request):
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    return render(request, "student/show.html", {"userNum": userNum})


def equipmentlist(request):
    """设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    equipments = models.Equipment.objects.all()
    return render(request, "student/equipmentlist.html", {"equipments": equipments})


def kindjsj(request):
    """计算机类设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    equipments = models.Equipment.objects.all().filter(eKind="计算机类")
    return render(request, "student/kindjsj.html", {"equipments": equipments})


def kindsw(request):
    """生物类设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    equipments = models.Equipment.objects.all().filter(eKind="生物类")
    return render(request, "student/kindsw.html", {"equipments": equipments})


def kindhx(request):
    """化学类设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    equipments = models.Equipment.objects.all().filter(eKind="化学类")
    return render(request, "student/kindhx.html", {"equipments": equipments})


def kindwl(request):
    """物理类设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    equipments = models.Equipment.objects.all().filter(eKind="物理类")
    return render(request, "student/kindwl.html", {"equipments": equipments})


def kindjx(request):
    """机械类设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    equipments = models.Equipment.objects.all().filter(eKind="机械类")
    return render(request, "student/kindjx.html", {"equipments": equipments})


def kindqt(request):
    """其它类设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    equipments = models.Equipment.objects.all().filter(eKind="其它类")
    return render(request, "student/kindqt.html", {"equipments": equipments})


def myequipment(request):
    """我借用的设备列表"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    user = models.User.objects.get(userNum=userNum)
    equipments = models.Equipment.objects.all().filter(eStudent=user)
    return render(request, "student/myequipment.html", {"equipments": equipments})


def borrow(request):
    """借用设备"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    eid = request.GET["eid"]
    equipment = models.Equipment.objects.get(id=eid)
    equipment.eState = "借出"
    user = models.User.objects.get(userNum=userNum)
    user.useCount += 1
    equipment.eStudent = user
    print(user.useCount)
    if user.useCount == 4:
        return HttpResponse("每人最多只可以同时借三件设备！")
    else:
        try:
            user.save()
            equipment.save()
        except Exception:
            return HttpResponse("借用失败！")
        else:
            return HttpResponse("借用成功！")


def returnback(request):
    """归还设备"""
    userNum = request.session.get("userNum")
    request.session["userNum"] = userNum
    eid = request.GET["eid"]
    user = models.User.objects.get(userNum=userNum)
    equipment = models.Equipment.objects.get(id=eid)
    equipment.eState = "待确认"
    try:
        models.Applylist.objects.create(student=user, equipment=equipment)
        equipment.save()
    except Exception:
        return HttpResponse("归还失败！")
    else:
        return HttpResponse("归还成功，请等待管理员确认！")
