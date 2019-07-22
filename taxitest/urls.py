from django.urls import path
from taxitest import views

# index及其Ajax更新
urlpatterns = [
    path('', views.index, name='index'),
    path('index_fresh/', views.index_fresh, name="index_fresh"),
]

# 数据检索页面
urlpatterns += [
    path('all_cars/', views.CarList.as_view(), name='all_cars'),
    path('all_clients/', views.all_clients, name='all_clients'),
    path('all_orders/', views.OrderList.as_view(), name='all_orders'),
]

urlpatterns += [
    path('address/', views.address, name='address'),
    path('car_fresh/', views.car_fresh, name="car_fresh"),
]
