from django.db import models

# Create your models here.

class Profile (models.Model):
    accountID = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    telephone = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.accountID
    
class Balance (models.Model):
    accountID = models.CharField(max_length=256)
    money = models.FloatField()
    credit = models.FloatField()
    
    def __str__(self):
        return self.accountID

class Account (models.Model):
    accountID = models.CharField(max_length=256)
    accountPin = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    profile = models.ForeignKey(Profile, related_name='profile')
    safeQuestion = models.CharField(max_length=256)
    safeAnswer = models.CharField(max_length=256)
    balance = models.OneToOneField(Balance, related_name='account')
    
    def __str__(self):
        return self.accountID
class Bank (models.Model):
    bankID = models.CharField(max_length=256)
    bankName = models.CharField(max_length=256)
    account = models.ForeignKey(Account, related_name='bank')
    profile = models.ForeignKey(Profile, related_name='bank')
    
class Notification (models.Model):
    accountID = models.CharField(max_length=256)
    fromAccount = models.ForeignKey(Account, related_name='account')
    date = models.DateTimeField(null=True)
    information = models.CharField(max_length=2048)
    
    def __str__(self):
        return self.accountID
    
