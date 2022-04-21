from django.contrib import admin
from FetchData.models import User,PatientDetails,CustomerDetails
# Register your models here.

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','Email','Password')
@admin.register(PatientDetails)

class PatientDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','name','Email','DateTime','RoomTemp','Humidity','BodyTemp')
    
    
@admin.register(CustomerDetails)
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','name','Email','DateTime','Order')
