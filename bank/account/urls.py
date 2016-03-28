from django.conf.urls import include, patterns, url
from account import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bank', views.BankViewSet)
router.register(r'account', views.AccountViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'balance', views.BalanceViewSet)
router.register(r'notification', views.NotificationViewSet)

urlpatterns = [
    # REST api
    url(r'^api/', include(router.urls)),
]