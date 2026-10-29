from django.contrib import admin
from django.urls import path
from bus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.login,name="login"),
    path('create-user/',views.createaccount,name="create-user"),
    path('busbooking/',views.bus_booking,name="booking"),

    path('bus_search/',views.bus_search,name="bus_search"),
    path('ticket/', views.ticket, name="ticket"),

]
