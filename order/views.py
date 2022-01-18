from django.shortcuts import render
from order.models import Shop, Menu, Order, Order_food
from order.serializer import ShopSerializer, MenuSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt  # 보안 적인 것,가로채기안되게끔
def shop(request):
    if request.method == 'GET':
        shop = Shop.objects.all()
        return render(request,'order/shop_list.html',{'shop_list':shop})
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt  # 보안 적인 것,가로채기안되게끔
def menu(request , shop):
    if request.method == 'GET':
        menu = Menu.objects.filter(Shop=shop)
        serializer = MenuSerializer(menu, many=True)  # 데이터를 json 파일 의 형태로 바꿔준다.
        return render(request,'order/menu_list.html',{'menu_list':menu})
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
