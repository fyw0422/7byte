from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^codes$', views.codes, name='codes'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^services1$', views.services1, name='services1'),
    url(r'^services2$', views.services2, name='services2'),
    url(r'^services3$', views.services3, name='services3'),
    url(r'^services4$', views.services4, name='services4'),
    url(r'^services5$', views.services5, name='services5'),
    url(r'^services6$', views.services6, name='services6'),
    url(r'^about$', views.about, name='about'),
    url(r'^code$', views.code, name='code'),


]