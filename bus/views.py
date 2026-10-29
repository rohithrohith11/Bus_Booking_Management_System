import email
from django.contrib import messages
from email.mime import message

from django.shortcuts import render,redirect,get_object_or_404

from bus.models import Createuser, Buses_available


# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']

        user=Createuser.objects.filter(name=name,password=password).first()

        if user:
            messages.success(request,"Successfully login!")
            return redirect('booking')
        else:
            messages.error(request,"Username/Password Not Existing!!!")

    return render(request,"login.html")

def createaccount(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        age=request.POST['age']
        mail=request.POST['email']
        phone=request.POST['phone']

        Createuser.objects.create(
            name=name,
            password=password,
            age=age,
            email=mail,
            phone=phone
        )
        return redirect('login')

    return render(request,"createaccount.html")

def bus_booking(request):
    if request.method=='POST':
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        city=request.POST.get("city")
        destination=request.POST.get("destination")
        passengers=request.POST.get("passengers")
        booking_date=request.POST.get("booking_date")
        booking_time=request.POST.get("booking_time")

        buses=Buses_available.objects.filter(departure=city,destinations=destination,avail_date=booking_date,avail_time=booking_time)

        context={
            "name":name,
            "phone":phone,
            "email":email,
            "city":city,
            "destinations":destination,
            "passengers":passengers,
            "booking_date":booking_date,
            "booking_time":booking_time,
            "buses":buses,
        }

        return render(request,"bus_Search.html",context)

    return render(request,"bus_booking.html")

"""def add_bus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        departure=request.POST.get('departure')
        destination=request.POST.get('destination')
        price=request.POST.get('price')
        avail_time=request.POST.get('avail_time')
        avail_date=request.POST.get('avail_date')

        Buses_available.objects.create(
            name=name,
            departure=departure,
            destinations=destination,
            price=price,
            avail_time=avail_time,
            avail_date=avail_date
        )
        return redirect('booking')
    return render(request,"add_bus.html")"""

def bus_search(request):
    return render(request,"bus_Search.html")

def ticket(request):
    if request.method=='POST':

        bus_id=request.POST.get("bus_id")

        bus=get_object_or_404(Buses_available,id=bus_id)

        context={
            "name":request.POST.get("name"),
            "phone":request.POST.get("phone"),
            "email":request.POST.get("email"),
            "city":request.POST.get("city"),
            "destinations":request.POST.get("destinations"),
            "booking_date":request.POST.get("booking_date"),
            "booking_time":request.POST.get("booking_time"),
            "bus":bus
        }
        return render(request,"ticket.html",context)

    return redirect("booking")


