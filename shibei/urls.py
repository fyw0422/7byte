from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('^shibei_web/', include('shibei_web.urls', namespace='shibei_web')),
    url('^shibei_admin/', include('shibei_admin.urls', namespace='shibei_admin')),
]