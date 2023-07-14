from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from .serializers import *
from .models import *
from .forms import *



def membershipFormQuote(request):

    try:
        membership_id = request.session['membership_id']
    except: 
        membership_id = None
    
    if membership_id:
        request.session['membership_id'] = None
    
    else:    
        cp = CompanyProfile.objects.first()
        form = MembershipForm()
        covers = Cover.objects.all()
        crisis_cover = Cover.objects.filter(category__name__icontains="crisis").first()
        orange_zone_cover = OrangeZoneCover.objects.first()
        
        covers_description = covers[0].category.description
        orange_zone_cover_description = orange_zone_cover.description
        crisis_covers_description = crisis_cover.category.description
    
    
    if request.method == "POST":
        if request.POST.get('crisis_cover') == 'on':
            crisis_cover = 1
        else:
            crisis_cover = 2
            
        days_in_orange_zone = request.POST.get("days_in_orange_zone")
        
        if not days_in_orange_zone:
            days_in_orange_zone = 0
            
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        membership = Membership.objects.create(
            membership_id = f"{timestamp}" ,
            start_date = request.POST.get('start_date'),
            days = request.POST.get('days'),
            person = request.POST.get('persons'),
            days_in_orange_zone = days_in_orange_zone,
            total_amount = float(request.POST.get('total_amount')[1:])
        )
        
        request.session['membership_id'] = membership.membership_id
        
        return redirect('app:membership-info')
    
    
    context = {
        'cp' : cp,
        'form' : form,
        'covers' : covers,
        'crisis_cover' : crisis_cover,
        'orange_zone_cover' : orange_zone_cover,
        'covers_description' : covers_description,
        'crisis_covers_description' : crisis_covers_description,
        'orange_zone_cover_description' : orange_zone_cover_description,
    }
    return render(request, 'membership-quote.html', context)


def membershipFormInfo(request):
    cp = CompanyProfile.objects.first()
    try:
        membership_id = request.session['membership_id']
    except: 
        return redirect('app:membership-quote')
    
    membership = Membership.objects.get(membership_id=membership_id)
    if request.method == 'POST':
        first_name = request.POST.getlist('first_name')
        last_name = request.POST.getlist('last_name')
        company = request.POST.getlist('company')
        country = request.POST.getlist('country')
        email = request.POST.getlist('email')
        phone_number = request.POST.getlist('phone_number')
        dob = request.POST.getlist('dob')
        gender = request.POST.getlist('gender')
        emergency_contact_number = request.POST.getlist('emergency_contact_number')
        emergency_contact_name = request.POST.getlist('emergency_contact_name')
        
        for i in range(membership.person):
            MembershipPerson.objects.create(
                membership = membership,
                first_name = first_name[i],
                last_name = last_name[i],
                company = company[i],
                country_of_residence = country[i],
                email = email[i],
                phone_number = phone_number[i],
                date_of_birth = dob[i],
                gender = gender[i],
                emergency_contact_phone = emergency_contact_number[i],
                emergency_contact_name = emergency_contact_name[i],
            )
        return redirect('app:membership-payment')
    
    context = {
        'cp' : cp,
        'membership' : membership,
        'persons' : membership.person,
    }
    return render(request, 'membership-info.html', context)




def membershipFormPayment(request):
    cp = CompanyProfile.objects.first()
    try:
        membership_id = request.session['membership_id']
    except: 
        return redirect('app:membership-quote')
    
    membership = Membership.objects.get(membership_id=membership_id)
    
    if request.method == "POST":
        first_name = request.POST.getlist('first_name')
        last_name = request.POST.getlist('last_name')
        address = request.POST.getlist('address')
        city = request.POST.getlist('city')
        country = request.POST.getlist('country')
        postal_code = request.POST.getlist('postal_code')
        referral_code = request.POST.getlist('referral_code')
        
        
        
        
    
    context = {
        'cp' : cp,
        'membership' : membership,
    }
    return render(request, 'membership-payment.html', context)






def referralCodeVerfication(request):
    code = request.GET.get('code')
    total = request.GET.get('total')
    
    
    if code != " ":
        result = ReferralCode.objects.filter(code=code).first()
        if result:
            discount_percentage = result.discount_percentage
            discounted_amount = float(total) - ((float(total)*discount_percentage)/100)
        else:
            discount_percentage = 0
            discounted_amount = 0
    
    data = {
        'discount_percentage' : discount_percentage,
        'discounted_amount' : discounted_amount
    }
    return JsonResponse(data)