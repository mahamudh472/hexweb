from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime


def membershipFormQuote(request):
    return render(request, 'membership-quote.html')

def membershipFormInfo(request):
    return render(request, 'membership-info.html')

def membershipFormPayment(request):
    return render(request, 'membership-payment.html')
