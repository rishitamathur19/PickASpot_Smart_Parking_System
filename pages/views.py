from django.shortcuts import render
from django.contrib import messages
from pages.models import registertable, usertable
import requests

def signin(request):
    return render(request,'sign-in.html')

def signup(request):
    return render(request,'sign-up.html')

def dashboard(request):
    return render(request,'dashboard.html')

def homepage(request):
    return render(request,'user-dashboard.html')

def parking_history(request):
    records = {}
    uid = request.session["logid"]
    url = "https://pickaspotgpg.000webhostapp.com/API/ADMINAPI/showbookings.php"
    params = {
        'logid': uid

    }
    r2 = requests.post(url=url, data=params)
    print(r2.text)

    res = r2.json()
    ev = res['error']
    records["history"] = res["parking"]
    print(records)
    return render(request,'parking-history.html',records)

def card_history(request):
    records = {}
    uid = request.session["logid"]
    url = "https://pickaspotgpg.000webhostapp.com/API/ADMINAPI/fetchrfidbookings1.php"
    params = {
        'logid': uid

    }
    r2 = requests.post(url=url, data=params)
    print(r2.text)

    res = r2.json()
    ev = res['error']
    records["history"] = res
    print(records)
    return render(request,'card-history.html',records)

def available_slots(request):
    records = {}
    url = requests.get("https://pickaspotgpg.000webhostapp.com/API/ADMINAPI/showparkings.php")
    data = url.json()
    records['parking'] = data
    return render(request,'available-slots.html',records)

def profile(request):
    return render(request, 'profile.html')

def cardinfo(request):
        return render(request, 'card-info.html')

def slot_booking(request):
    records = {}
    url = requests.get("https://pickaspotgpg.000webhostapp.com/API/ADMINAPI/showparkings.php")
    data = url.json()
    records['parking'] = data
    print(records)
    return render(request, 'slot-booking.html',records)

def bookingdata(request):
    if request.method == 'POST':
        uid = request.session["logid"]
        userbookdate = request.POST.get("bookdate")
        userbooktime = request.POST.get("booktime")
        parking = request.POST.get("parking")

        url = "https://pickaspotgpg.000webhostapp.com/API/ADMINAPI/bookslot.php"
        params = {
            'LOGIN_ID': uid,
            'PARKING_ID': parking,
            'DATE': userbookdate,
            'TIME': userbooktime,

        }
        r2 = requests.post(url=url, data=params)
        print(r2.text)

        res = r2.json()
        ev = res['error']
        if not ev:
            messages.error(request, "Slot Booked")
            return render(request, 'parking-history.html')
        else:
            messages.error(request, "error occured !! ")
    else:
        pass
    return render(request, 'slot-booking.html')

def updateprofile(request):
    return render(request, 'update-profile.html')

def smoketable(request):
    records = {}
    url = requests.get("https://pickaspotgpg.000webhostapp.com/API/smoke_sensor_data.php")
    data = url.json()
    records['smoke'] = data
    return render(request, 'smoke-table.html',records)

def ultrasonictable(request):
    records = {}
    url = requests.get("https://pickaspotgpg.000webhostapp.com/API/ultrasonic_sensor_data.php")
    data = url.json()
    records['ultrasonic'] = data
    return render(request, 'ultrasonic-table.html',records)

def irtable(request):
    records = {}
    url = requests.get("https://pickaspotgpg.000webhostapp.com/API/ir_sensor_data.php")
    data = url.json()
    records['ir'] = data
    return render(request, 'ir-table.html',records)

def rfidtable(request):
    records = {}
    url = requests.get("https://pickaspotgpg.000webhostapp.com/API/rfid_sensor_data.php")
    data = url.json()
    records['rfid'] = data
    return render(request, 'rfid-table.html',records)

def firetable(request):
    records = {}
    url = requests.get("https://pickaspotgpg.000webhostapp.com/API/fire_sensor_data.php")
    data = url.json()
    records['fire'] = data
    return render(request, 'fire-table.html',records)


def signout(request):
    try:
        del request.session['logid']
        del request.session['logname']
        del request.session['logemail']
    except:
        pass
    messages.info(request, "logout!!")
    return render(request, 'sign-in.html')

def fetchdata(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        usermail = request.POST.get("umail")
        userphone = request.POST.get("uphone")
        userpass = request.POST.get("upass")

        url = "https://pickaspotgpg.000webhostapp.com/API/ADMINAPI/SIGNUP(PROJECT).php"
        params = {
            'NAME': username,
            'PHONE_NO': userphone,
            'EMAIL_ID':usermail,
            'PASSWORD':userpass,

        }
        r2 = requests.post(url=url, data=params)
        print(r2.text)

        res = r2.json()
        ev = res['error']
        if not ev:
            messages.error(request, "Registered Successfully")
            return render(request, 'sign-in.html')
        else:
            messages.error(request, "error occured !! ")
    else:
        pass
    return render(request,'sign-in.html')

def checkdata(request):
    if request.method == 'POST':
        email = request.POST.get("EMAIL_ID")
        password = request.POST.get("PASSWORD")

        url = "https://pickaspotgpg.000webhostapp.com/API/ADMINAPI/LOGIN(PROJECT).php"
        params = {
            "EMAIL_ID": email,
            "PASSWORD": password
        }
        r2 = requests.post(url=url, data=params)
        print(r2.text)

        res = r2.json()
        ev = res['error']
        if not ev:
            uid = res['user']['LOGIN_ID']
            uname = res['user']['NAME']
            uemail = res['user']['EMAIL_ID']
            ukey = res['user']['RFIDKEY']
            request.session['logid'] = uid
            request.session['logname'] = uname
            request.session['logemail'] = uemail
            request.session["rfidkey"] = ukey
            request.session.save()
            messages.info(request, "Successfully logged in!!")
            return render(request, 'dashboard.html')
        else:
            messages.error(request, "Invalid Email & Password !! ")

    else:
        messages.error(request, "Unable to Login..!!")
    return render(request, "sign-in.html")
