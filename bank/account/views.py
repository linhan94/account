from django.shortcuts import render

from .models import Bank, Account, Profile, Balance, Notification
# Create your views here.

# REST imports
from rest_framework import viewsets
from .serializers import BankSerializer, AccountSerializer, ProfileSerializer, BalanceSerializer, NotificationSerializer

class BankViewSet (viewsets.ModelViewSet):
    queryset = Bank.objects.order_by('bankID')
    serializer_class = BankSerializer
    
class AccountViewSet (viewsets.ModelViewSet):
    queryset = Account.objects.order_by('accountID')
    serializer_class = AccountSerializer
    
class ProfileViewSet (viewsets.ModelViewSet):
    queryset = Profile.objects.order_by('accountID')
    serializer_class = ProfileSerializer
    
class BalanceViewSet (viewsets.ModelViewSet):
    queryset = Balance.objects.order_by('accountID')
    serializer_class = BalanceSerializer
    
class NotificationViewSet (viewsets.ModelViewSet):
    queryset = Notification.objects.order_by('accountID')
    serializer_class = NotificationSerializer