import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Auth, Role, User


def addauth(request):
    auth = Auth()
    auth.auth_name = 'auth%s' %random.randrange(100)
    auth.save()
    return HttpResponse('add auth success')

def addrole(request):
    role = Role()
    role.role_name = 'role%s'%random.randrange(100)
    role.save()
    return HttpResponse('add role success')

def adduser(request):
    user = User()
    user.user_name = 'tom%s'%random.randrange(100)
    user.save()
    return HttpResponse('user add success')

def add_role_auth(request):
    roles = list(Role.objects.all())
    auths = list(Auth.objects.all())

    # for role in roles:
    #     auth_list = random.sample(auths, random.randrange(len(auths)) + 1)
    #     for auth in auth_list:
    #         role.auth.add(auth)
    return HttpResponse('role_auth add success')

def add_user_role(request):
    users = list(User.objects.all())
    roles = list(Role.objects.all())

    # for user in users:
    #     role_list = random.sample(roles, random.randrange(len(roles)) + 1)
    #     for role in roles:
    #         user.role.add(role)
    return HttpResponse('user_role add success')

def check_load(request):
    users = User.objects.all()
    roles = Role.objects.all()

    return render(request, 'admin.html', {'roles':roles, 'users':users})


def check_role(request):
    users = User.objects.all()
    roles = Role.objects.all()

    roleid = request.POST.get('role_id')
    role = Role.objects.filter(id = roleid)
    auths = role[0].auth.all()
    return render(request, 'admin.html', {'role_name':role[0].role_name ,'auths':auths,'roles':roles, 'users':users})


def check_user(request):
    pass

def auth_role(request):
    auth = Auth.objects.first()
    roles = auth.role_set.all()
    print(roles)
    return HttpResponse('success')
