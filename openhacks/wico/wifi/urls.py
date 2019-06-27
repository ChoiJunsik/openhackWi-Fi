from django.urls import path
from . import views

app_name = 'wifi'

urlpatterns = [
    # path('',views.main,name='main'),
    path('maclist/',views.macList, name='macList'),
    path('date/',views.getDate, name='date'),
    path('machour/',views.getMacHour, name='machour'),
    path('devicecount/', views.deviceCount, name = 'devicecount'),
]