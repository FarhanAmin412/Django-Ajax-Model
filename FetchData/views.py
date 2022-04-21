import datetime
from xmlrpc.client import DateTime
from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import PatientRegistration,CustomerDetailsRegistration
from .models import CustomerDetails, User,PatientDetails
# Create your views here.

RT = "None"
HM = "None"
BT = "None"

def FetchDataFromThingspeak(request):
    return render(request,'FetchData/Thingspeak.html')

def prototypes(request):
    return render(request, 'FetchData/Prototype.html')
    

# This Function Adds and Displays all Items
def add_show(request):
    if request.method == 'POST':
        fm = PatientRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['Email']
            pw = fm.cleaned_data['Password']
            register = User(name=nm,Email=em,Password=pw)
            register.save()
            fm = PatientRegistration()
    else:
        fm = PatientRegistration()
    patient = User.objects.all()
    return render(request,'FetchData/addandshow.html',{'form':fm, 'pat':patient})

def add_show_Customer(request):
    if request.method == 'POST':
        now = datetime.datetime.now() 
        ok_date = (str(now.strftime("%Y-%m-%d %H:%M:%S.%f")))
        ok_date = ok_date[:-4]
        fm = CustomerDetailsRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['Email']
            order = fm.cleaned_data['Order']
            register = CustomerDetails(name=nm,Email=em,DateTime=ok_date,Order=order)
            register.save()
            fm = CustomerDetailsRegistration()
    else:
        fm = CustomerDetailsRegistration()
    customer = CustomerDetails.objects.all()
    return render(request,'FetchData/addAndShowCus.html',{'form':fm, 'cus':customer})


# This function will delete data
def delete_data(request,id):
    if request.method == 'POST':
        pid = User.objects.get(pk=id)
        pid.delete()
        return HttpResponseRedirect('/FetchData/AddandShow')
    
def delete_data_Customer(request,id):
    if request.method == 'POST':
        pid = CustomerDetails.objects.get(pk=id)
        pid.delete()
        return HttpResponseRedirect('/FetchData/AddandShowCustomer')

def delete_PatientDetails(request,id):
    if request.method == 'POST':
        P_id = PatientDetails.objects.get(pk=id)
        P_id.delete()
        return HttpResponseRedirect('/FetchData/Login')

# This function will edit Patient Information
def update_data(request,id):
    if request.method == 'POST':
        pid = User.objects.get(pk=id)
        fm = PatientRegistration(request.POST, instance=pid)
        if fm.is_valid():
            fm.save()
    else:
        pid = User.objects.get(pk=id)
        fm = PatientRegistration(instance=pid)
    return render(request,'FetchData/UpdatePatient.html',{'form':fm})

def update_data_Customer(request,id):
    if request.method == 'POST':
        pid = CustomerDetails.objects.get(pk=id)
        fm = CustomerDetailsRegistration(request.POST, instance=pid)
        if fm.is_valid():
            fm.save()
    else:
        pid = CustomerDetails.objects.get(pk=id)
        fm = CustomerDetailsRegistration(instance=pid)
    return render(request,'FetchData/UpdateCustomer.html',{'form':fm})

# This Function provides Login for Patient
def login(request):
    if request.method == 'POST':
        fm = PatientRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['Email']
            pw = fm.cleaned_data['Password']
            context = {'form':fm,'Name':nm,'Email':em,'Password':pw}
            fm = PatientRegistration()
    else:
        fm = PatientRegistration()
        context = {'form':fm,'Name':'Enter Name','Email':'Enter Email'}
    return render(request,'FetchData/Login.html',context)    
    
    
    
def VitalDetailsPatient(request,Name,Email):
    now = datetime.datetime.now() 
    ok_date = (str(now.strftime("%Y-%m-%d %H:%M:%S.%f")))
    ok_date = ok_date[:-4]
    P_Details = PatientDetails(name=Name,Email=Email,DateTime=ok_date,RoomTemp=RT(),Humidity=HM(),BodyTemp=BT())
    P_Details.save()
    P = PatientDetails.objects.all()                
    return render(request,'FetchData/PatientDetails.html',{'pat':P})





def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def getData(request,Name,Email): 
     import urllib.request 
     import json 
     data = {} 
     sensor_data = [] 
     if is_ajax(request=request): 
            now = datetime.datetime.now() 
            ok_date = (str(now.strftime("%Y-%m-%d %H:%M:%S.%f")))
            ok_date = ok_date[:-4]
            custom_url = request.GET.get('id', None)   
            try: 
                with urllib.request.urlopen(custom_url) as url:s = url.read() 
                data = json.loads(s) 
                if data: 
                    sensor_data = {
                   'name': str(Name),
                   'email': str(Email),
                   'date': str(ok_date), 
                   'temp': data['feeds'][1]['field1'],  'humidity': data['feeds'][1]['field2'], 'bodytemp': data['feeds'][1]['field3']
                   }
                    global RT
                    def RT():
                        return data['feeds'][1]['field1']
                    global HM
                    def HM():
                        return data['feeds'][1]['field2']
                    global BT
                    def BT():
                        return data['feeds'][1]['field3']  
                else: 
                    sensor_data = {
                    'name': str(Name),
                    'email': str(Email),    
                    'date': str(ok_date), 
                    'temp': 'No Data', 
                    'humidity': 'No Data',
                    'bodytemp': 'No Data',} 
  
            except Exception as x: 
                    sensor_data = { 
                    'date': str(ok_date),
                    'name': str(Name),
                    'email': str(Email), 
                    'temp': 'Network Error', 
                    'humidity': 'Network Error',
                    'bodytemp': 'Network Error',}
            data['result'] = sensor_data 
     else: 
        data['result'] = "Not Ajax" 
     return JsonResponse(data) 

