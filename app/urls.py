from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('home.html',views.home,name="home"),
    path('ru.html',views.ru,name="ru"),
    path('ar.html', views.ar, name="ar"),
    path('tr.html', views.tr, name="tr"),
    path('iso9001.html', views.iso9001, name="iso9001"),
    path('iso10002.html', views.iso10002, name="iso10002"),
    path('iso10004.html', views.iso10004, name="iso10004"),
    path('enexportnews.html', views.enexportnews, name="enexportnews"),
    path('enindustrynews.html', views.enindustrynews, name="enindustrynews"),
    path('eneconomicsnews.html', views.eneconomicsnews, name="eneconomicsnews"),
    path('news.html', views.news, name="news"),
]

