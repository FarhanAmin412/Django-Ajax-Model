from django.urls import path
from . import views

urlpatterns = [
    path('Th/<str:Name>/<str:Email>/',views.getData,name='getData'),
    path('<str:Name>/<str:Email>/',views.FetchDataFromThingspeak,name='FetchData'),
    path('AddandShow/',views.add_show,name='AddandShow'),
    path('AddandShowCustomer/',views.add_show_Customer,name='AddandShowCustomer'),
    path('Login/',views.login,name='Login'),
    path('CheckVitals/<str:Name>/<str:Email>',views.VitalDetailsPatient,name='CheckVitals'),
    path('<int:id>/',views.update_data_Customer,name="updatedataCustomer"),
]