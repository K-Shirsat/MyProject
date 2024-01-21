from django.shortcuts import render,redirect
from .models import Product,Orders,Customer
from .forms import OrderForm

# Create your views here.

def dashboard(request):
    customer=Customer.objects.all()
    orders=Orders.objects.all()
    total=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    
    context={
        "customer":customer,
        "orders":orders,
        "total":total,
        "delivered":delivered,
        "pending":pending,
        
        
    }
    return render(request,"Dapp/dashboard.html",context)

def product(request):
    item=Product.objects.all()
    context={
        "item":item,}    
    return render(request,"Dapp/product.html",context)

def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    order=customer.orders.all()
    order_count=order.count()
    context={
        'pk_test':pk_test,
        'customer':customer,
        'order':order, 'order_count':order_count        
    }
    return render(request,"Dapp/customer.html",context)

def createOrder(request):
    form=OrderForm()
    if request.method=="POST":
         form=OrderForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/')
    context={'form':form}
    return render(request,"Dapp/order_create.html",context)

def updateOrder(request,pk):
    order=Orders.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
         form=OrderForm(request.POST,instance=order)
         if form.is_valid():
             form.save()
             return redirect('/')
    context={'form':form,}
    return render(request,"Dapp/order_create.html",context)

def deleteOrder(request,pk):
    order=Orders.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'order':order,}
    return render(request,"Dapp/delete.html",context)
