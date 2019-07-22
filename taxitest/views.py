from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
# Create your views here.
from .models import Car, Client, Order

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_cars=Car.objects.all().count()
    num_clients=Client.objects.all().count()
    num_orders=Order.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        #context={'num_cars':num_cars,'num_clients':num_clients,'num_orders':num_orders},
    )


from django.views import generic
class CarList(generic.ListView):
    model = Car
'''
class ClientList(generic.ListView):
    model = Client
'''
class OrderList(generic.ListView):
    model = Order

#用户信息列表，包含查询，分页功能
def all_clients(request):
    # q=request.GET.get('name_or_number')

    client_list = Client.objects.all()
    # else:
    #     client_list = Client.objects.filter(client_name__icontains=q)
    #     if not client_list:
    #         client_list = Client.objects.filter(phone_number__icontains=q)
    return render(request, 'taxitest/client_list.html', {'client_list': client_list})
'''
    paginator = Paginator(client_list, 3)

    # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
    page = request.GET.get('page')
    try:
        clients = paginator.page(page)
    # todo: 注意捕获异常
    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        clients = paginator.page(1)
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        return HttpResponse('找不到页面的内容') 
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        clients = paginator.page(paginator.num_pages)
'''



#Ajax动态更新
from django.http import JsonResponse
def index_fresh(request):

    context = {"num_cars":Car.objects.all().count(),
        "num_clients":Client.objects.all().count(),
        "num_orders":Order.objects.count()}
    return JsonResponse(context)

import json
from django.utils.safestring import mark_safe
def address(request):
    # address_point = address_info.objects.all()
    position_x = []
    position_y = []
    address_data = []
    car = Car.objects.all()

    for i in range(len(car)):
        position_x.append(car[i].current_position_x)
        position_y.append(car[i].current_position_y)
        address_data.append([ car[i].car_id, car[i].current_velocity, car[i].tire_pressure_left_front, car[i].tire_pressure_right_front,
        car[i].tire_pressure_left_behind, car[i].tire_pressure_right_behind, car[i].camera_status, car[i].lidar_status, car[i].ibeo_status])

    return render(request, 'address.html',
        {'position_x': json.dumps(position_x),
        'position_y': json.dumps(position_y),
        'address_data':mark_safe(json.dumps(address_data))})

def car_fresh(request):

    address_data = []
    car = Car.objects.all()
    position_x = []
    position_y = []
    address_data = []

    for i in range(len(car)):
        position_x.append(car[i].current_position_x)
        position_y.append(car[i].current_position_y)
        address_data.append([ car[i].car_id, car[i].current_velocity, car[i].tire_pressure_left_front, car[i].tire_pressure_right_front,
        car[i].tire_pressure_left_behind, car[i].tire_pressure_right_behind, car[i].camera_status, car[i].lidar_status, car[i].ibeo_status])

    context = {
        "position_x":position_x,
        "position_y":position_y,
        "address_data":address_data
    }
    return JsonResponse(context)