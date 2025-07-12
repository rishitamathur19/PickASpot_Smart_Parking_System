from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name="login"),
    path('signup',views.signup,name="signup"),
    path('dashboard',views.dashboard,name="home"),
    path('homepage',views.homepage,name="homepage"),
    path('profile',views.profile,name="profile"),
    path('updateprofile',views.updateprofile,name="updateprofile"),
    path('parking_history',views.parking_history,name="parking_history"),
    path('card_history',views.card_history,name="card_history"),
    path('available_slots', views.available_slots, name="available_slots"),
    path('slot_booking', views.slot_booking, name="slot_booking"),
    path('bookingdata',views.bookingdata,name="bookingdata"),
    path('smoketable',views.smoketable,name="smoketable"),
    path('ultrasonictable',views.ultrasonictable,name="ultrasonictable"),
    path('rfidtable',views.rfidtable,name="rfidtable"),
    path('irtable',views.irtable,name="irtable"),
    path('firetable',views.firetable,name="firetable"),
    path('cardinfo',views.cardinfo,name="cardinfo"),
    path('fetchdata',views.fetchdata,name="fetchdata"),
    path('checkdata',views.checkdata,name="checkdata"),
    path('signout',views.signout,name="signout")
]