from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

from .views import HomeView, get_data, ChartData
urlpatterns  = [
    path('',views.index),
    path('data_analysis/',views.data_analysis),
    path('simplechart/',views.simplechart),
    path('base/',views.base),
    path('home/',views.home),
    path('bar_chart/',views.bar_chart),
    path('pie_chart/',views.pie_chart),
    path('scatter_chart/',views.scatter_chart),
    path('line_chart/',views.line_chart),
    path('gant_chart/',views.gant_chart),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^admin/', admin.site.urls),
    
    
]