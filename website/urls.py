from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.contact2, name='contact2'),
    path('seven.html', views.seven, name='seven'),
    
    path('about.html', views.about, name='about'),
    path('car.html', views.car, name='car'),
    path('contact.html', views.contact, name='contact'),
    path('detail.html', views.detail, name='detail'),
    path('service.html', views.service, name='service'),
    path('message.html', views.contact, name="contact"),
    
    path('meetings.html', views.meetings, name='meetings'),
    path('meeting-details.html', views.meetingdetails, name='meetingdetails'),
]
