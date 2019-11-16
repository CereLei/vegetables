from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import re
from user.models import User
# Create your views here.


def register(request):
  return render(request, 'register.html')


def register_handle(request):
    '''数据校验'''
	# 获取数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
	# 数据校验
     # 判断是否为空
    if not all([username,password,email]):
        return render(request,'register.html',{'errmsg':'数据不完整'})
    if allow != 'on':
        return render(request,'register.html',{'errmsg':'请勾选再提'})
	# 进行业务处理，注册
    ##  判断数据库是否已经存过
    try:
        user = User.objects.get(username= username)
    except User.DoesNotExist:
        user = None
    if user:
        return render(request,'register.html',{'errmsg':'用户名重复'})
    user = User.objects.create_user(username, email, password)
    # user.save()
	# 返回应答
    return redirect(reverse('goods:index'))
