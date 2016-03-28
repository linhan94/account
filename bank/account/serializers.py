from rest_framework import serializers
from .models import Bank, Account, Profile, Balance, Notification

#Using HyperlinkedModelSerializers
class BankSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ('bankID', 'bankName', 'account','profile')
        
class AccountSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('accountID', 'accountPin', 'password', 'profile', 'safeQuestion', 'safeAnswer', 'balance')
    
class ProfileSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('accountID', 'name', 'address', 'telephone', 'email')

class BalanceSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Balance
        fields = ('accountID', 'money', 'credit')

class NotificationSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ('accountID', 'fromAccount', 'date', 'information')
