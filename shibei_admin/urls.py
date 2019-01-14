# -*- coding: utf -8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^welcome$', views.welcome, name='welcome'),    # 一个后台登陆后的欢迎界面
    url(r'^login$', views.login, name='login'),     # 后台登陆页面

    # 新闻动态管理
    url(r'^journalismManagement$', views.journalismManagement, name='journalismManagement'),    # 新闻管理
    url(r'^addJournalism$', views.addJournalism, name='addJournalism'),    # 添加新闻
    url(r'^journalismInfo', views.journalismInfo, name='journalismInfo'),    # 查看新闻详情
    url(r'^editJournalism$', views.editJournalism, name='editJournalism'),    # 添加新闻

    # 合作伙伴管理
    url(r'^partnerManage$', views.partnerManage, name='partnerManage'),    # 合作伙伴
    url(r'^expectCooperation$', views.expectCooperation, name='expectCooperation'),    # 期待合作
    url(r'^addPartner$', views.addPartner, name='addPartner'),    # 添加合作伙伴
    url(r'^editPartner$', views.editPartner, name='editPartner'),    # 编辑合作伙伴

    # 产品问题管理
    url(r'^feedbackIssue $', views.feedbackIssue, name='feedbackIssue'),    # 历史问题
    url(r'^IssueInfo $', views.IssueInfo, name='IssueInfo'),    # 问题详情
    url(r'^editIssue $', views.editIssue, name='editIssue'),    # 编辑问题


    # 超级管理员
    url(r'^adminList$', views.adminList, name='adminList'),    # 管理员列表
    url(r'^addAdmin$', views.addAdmin, name='addAdmin'),    # 添加管理员
    url(r'^adminUpdatePassword $', views.adminUpdatePassword, name='adminUpdatePassword'),  # 修改密码
]