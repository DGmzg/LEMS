from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.contrib.auth.hashers import make_password, check_password


# 主页
def index(request):
    return render(request, 'user/index.html')


# 注册
def register(request):
    userName = request.POST['userName']
    userNum = request.POST['userNum']
    userPhone = request.POST['userPhone']
    userPwd1 = request.POST['userPwd1']
    userPwd2 = request.POST['userPwd2']

    # 判断两次密码是否一致
    if userPwd1 != userPwd2:
        return JsonResponse({"code": 1})
    # 判断输入是否合法
    try:
        int(userPhone)
        int(userNum)
    except ValueError:
        return JsonResponse({"code": 4})

    # 通过学号判断用户是否已经注册
    if models.User.objects.filter(userNum=userNum):
        return JsonResponse({"code": 2})
    else:
        # 注册信息
        models.User.objects.create(userName=userName, userNum=userNum, userPhone=userPhone,
                                   userPwd=make_password(userPwd1))
        return JsonResponse({"code": 3})


# 登录验证
def checklogin(request):
    userNum = request.POST['userNum']
    userPwd = request.POST['userPwd']
    request.session["userNum"] = userNum
    Flag = False
    # 查询是否已经注册
    if models.User.objects.filter(userNum=userNum):
        if models.User.objects.filter(userNum=userNum).get().userNum == "0":
            Flag = True
        # 查询密码是否正确
        if check_password(userPwd, models.User.objects.filter(userNum=userNum).get().userPwd):
            if Flag:
                # 教师登录成功
                return JsonResponse({"code": 0})
            else:
                # 学生登录成功
                return JsonResponse({"code": 1})
        else:
            # 密码错误
            return JsonResponse({"code": 2})
    else:
        # 用户不存在
        return JsonResponse({"code": 3})






