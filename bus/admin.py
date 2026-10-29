from django.contrib import admin
from bus.models import Bookings, Buses_available, User, Createuser


class bookingsadmin(admin.ModelAdmin):
    list_display = ['name','phone','email','booking_date','booking_time']

class busesavailableadmin(admin.ModelAdmin):
    list_display = ['name','departure','destinations','price','avail_time','avail_date']

class useradmin(admin.ModelAdmin):
    list_display = ['username','password']

class createuseradmin(admin.ModelAdmin):
    list_display = ['name','password','age','email','phone']

admin.site.register(Bookings,bookingsadmin)
admin.site.register(Buses_available,busesavailableadmin)
admin.site.register(User,useradmin)
admin.site.register(Createuser,createuseradmin)