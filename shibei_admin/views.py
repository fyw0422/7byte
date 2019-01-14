# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from collections import OrderedDict
from datetime import datetime
import uuid, json, math


def index(request):
    return render(request, "shibei_admin/index.html")


def welcome(request):
    return render(request, 'shibei_admin/welcome.html')


def login(request):
    return render(request, 'shibei_admin/login.html')


# 新闻动态管理
# ---------------------------------------------------#
# 新闻管理
def journalismManagement(request):
    return render(request, 'shibei_admin/journalismManagement.html')


# 添加新闻
def addJournalism(request):
    return render(request, 'shibei_admin/add_journalism.html')


# 查看新闻详情
def journalismInfo(request):
    return render(request, 'shibei_admin/journalism_info.html')


# 编辑新闻
def editJournalism(request):
    return render(request, 'shibei_admin/edit_journalism.html')


# 合作伙伴管理
# ---------------------------------------------------#
# 合作伙伴
def partnerManage(request):
    return render(request, 'shibei_admin/partner-brand.html')


# 期待合作
def expectCooperation(request):
    return render(request, 'shibei_admin/expect_cooperation.html')


# 添加合作伙伴
def addPartner(request):
    return render(request, 'shibei_admin/add_partner.html')


# 编辑合作伙伴
def editPartner(request):
    return render(request, 'shibei_admin/edit_partner.html')


# 产品问题管理
# ---------------------------------------------------#
# 历史问题
def feedbackIssue(request):
    return render(request, 'shibei_admin/feedback_issue.html')


# 问题详情
def IssueInfo(request):
    return render(request, 'shibei_admin/issue_info.html')


# 编辑问题
def editIssue(request):
    return render(request, 'shibei_admin/edit_issue.html')


# 管理员管理
# ---------------------------------------------------#
# 角色管理
def adminList(request):
    return render(request, 'shibei_admin/admin_list.html')


# 添加管理员
def addAdmin(request):
    return render(request, 'shibei_admin/add_admin.html')


# 修改密码
def adminUpdatePassword(request):
    return render(request, 'shibei_admin/admin_update_password.html')