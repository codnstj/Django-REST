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
def menu(request,shop):
    if request.method == 'GET':
        menu = Menu.objects.filter(Shop=shop)
        serializer = MenuSerializer(menu, many=True)  # 데이터를 json 파일 의 형태로 바꿔준다.
        return render(request,'order/menu_list.html',{'menu_list':menu,'shop':shop})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

from django.utils import timezone
@csrf_exempt  # 보안 적인 것,가로채기안되게끔
def order(request):
    if request.method == 'POST':
        address = request.POST['address']
        shop = request.POST['shop']
        food_list = request.POST.getlist('menu')
        order_date = timezone.now()

        shop_item = Shop.objects.get(pk=int(shop))

        shop_item.order_set.create(address = address , order_date=order_date , shop=int(shop))

        order_item = Order.objects.get(pk=shop_item.order_set.latest('id').id)
        for food in food_list:
            order_item.order_food_set.create(food_name=food)

        return render(request,'order/order_success.html')
    elif request.method == 'GET':
        order_list = Order.objects.all()
        return render(request,'order/order_list.html',{'order_list':order_list})