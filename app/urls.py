from django.urls import path
from .views import *


urlpatterns = [
    path('', membershipFormQuote, name="membership-quote"),
    path('info', membershipFormInfo, name="membership-info"),
    path('payment', membershipFormPayment, name="membership-payment"),
    
    path('referral-code-verification-ajaxt', referralCodeVerfication, name="referral-code-verification"),
]