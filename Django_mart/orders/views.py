from django.shortcuts import render

# Create your views here.
def oder_complete(request):
    return render(request, 'orders/order_complete.html')
def placeOrder(request):
    return render(request, 'orders/place-order.html')