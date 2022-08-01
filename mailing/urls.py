from django.contrib import admin
from django.urls import path
from .views import (
    HourView, DetailHourView,
    PhoneView, DetailPhoneView,
    UserView, DetailUserView,
    MailingView, DetailMailingView,
    MessageView, DetailMessageView
)

urlpatterns = [
    path('mailing/', MailingView.as_view(), name='mailing'),
    path('mailing/<int:pk>/', DetailMailingView.as_view(), name='mailing_id'),
    path('user/', UserView.as_view(), name='user'),
    path('user/<int:pk>/', DetailUserView.as_view(), name='user_id'),
    path('phone/', PhoneView.as_view(), name='phone'),
    path('phone/<int:pk>/', DetailPhoneView.as_view(), name='phone_id'),
    path('hour/', HourView.as_view(), name='user'),
    path('hour/<int:pk>/', DetailHourView.as_view(), name='user_id'),
    path('message/', MessageView.as_view(), name='message'),
    path('message/<int:pk>/', DetailMessageView.as_view(), name='message_id'),
]