from django.urls import path
from boss import views

urlpatterns = [
    path('orders/<int:shop>',views.order_list,name="order_list"),
    path('time_input/',views.time_input,name="time_input")
]