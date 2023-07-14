from django.db import models
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField

# Create your models here.



class CompanyProfile(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to='company profile/logo')
    favicon = models.ImageField(upload_to='company profile/favicon')

    class Meta:

        verbose_name = 'Company Profile'
        verbose_name_plural = 'Company Profile'

    def __str__(self):
        return self.title
    

class ServicesAgreement(models.Model):
    content = RichTextField()

    class Meta:

        verbose_name = 'Services Agreement'
        verbose_name_plural = 'Services Agreement'
    


class CoverCategory(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)

    class Meta:

        verbose_name = 'Cover Category'
        verbose_name_plural = 'Cover Categories'

    def __str__(self):
        return self.name


class Cover(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    category = models.ForeignKey(CoverCategory, on_delete=models.CASCADE, related_name='covers')
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    countries = CountryField(multiple=True)
    price_per_day = models.DecimalField(max_digits=9999, decimal_places=2)

    class Meta:

        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'

    def __str__(self):
        return self.name

    

    
class Affiliate(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    point_of_contact = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:

        verbose_name = 'Affiliate'
        verbose_name_plural = 'Affiliates'

    def __str__(self):
        return self.point_of_contact


class ReferralCode(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE, related_name='codes')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=300)
    discount_percentage = models.IntegerField()

    class Meta:

        verbose_name = 'Referral Code'
        verbose_name_plural = 'Referral Codes'

    def __str__(self):
        return self.name


class Membership(models.Model):
    payment_status = (
        (1, 'Incomplete'),
        (2, 'Complete'),
    )
    
    status = models.IntegerField(default=1, choices=payment_status)
    membership_id = models.CharField(max_length=300)
    start_date = models.DateField()
    days = models.IntegerField()
    country = CountryField(default="UA")
    person = models.IntegerField()
    days_in_orange_zone = models.IntegerField()
    crisis_cover = models.IntegerField(default=2)
    total_amount = models.DecimalField(decimal_places=2, max_digits=9999)
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.SET_NULL, null=True, blank=True)
    discounted_amout = models.DecimalField(decimal_places=2, max_digits=9999, null=True, blank=True)
    email_subscription = models.BooleanField(default=False)
    services_agreement = models.BooleanField(default=False)
    auto_revewal = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'Membership'
        verbose_name_plural = 'Memberships'

    def __str__(self):
        return self.membership_id



class MembershipPerson(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name='persons')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50, null=True, blank=True)
    country_of_residence = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_phone = models.CharField(max_length=30)
    membership_certificate = models.FileField(upload_to='membership_certficates', null=True)

    class Meta:

        verbose_name = 'Membership Person'
        verbose_name_plural = 'Membership Persons'

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class OrangeZoneCover(models.Model):
    percentage = models.IntegerField()
    description = RichTextField()

    class Meta:

        verbose_name = 'Orange Zone Cover'
        verbose_name_plural = 'Orange Zone Cover'

    def __str__(self):
        return 'Orange Zone Cover'



class MembershipPayment(models.Model):
    membership = models.OneToOneField(Membership, on_delete=models.CASCADE, related_name='related_payment')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    

    class Meta:

        verbose_name = 'Membership Payment'
        verbose_name_plural = 'Membership Payments'

    def __str__(self):
        return self.membership.membership_id


