# coding=utf-8
import os
from django.conf import settings
from django.urls import include, re_path
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ytenx.views import index_page, renew_session, about_page, zim, kiemx_sriek

urlpatterns = [
  re_path(r'^kyonh/', include('ytenx.kyonh.urls')),
  re_path(r'^tcyts/', include('ytenx.tcenghyonhtsen.urls')),
  re_path(r'^pyonh/', include('ytenx.pyonh.urls')),
  re_path(r'^trngyan/', include('ytenx.trngyan.urls')),
  re_path(r'^dciangx/', include('ytenx.dciangxkox.urls')),
  re_path(r'^byohlyuk/', include('ytenx.byohlyuk.urls')),
  re_path(r'^$', index_page, name='index_page'),
  re_path(r'^r$', renew_session, name='renew_session'),
  re_path(r'^about$', about_page, name='about_page'),
  re_path(r'^zim$', zim, name='zim'),
  re_path(r'^sriek$', kiemx_sriek, name='kiemx_sriek'),
  # Served by the app in every environment, since STATIC_URL may point at a CDN without this file.
  re_path(r'^(?P<path>rare-font\.css)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'ytenx', 'static', 'css')}, name='rare_font_css'),
]

urlpatterns += staticfiles_urlpatterns()
