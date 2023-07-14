from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('title',)
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
    
@admin.register(ServicesAgreement)
class ServicesAgreementAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    def title(self, obj):
        return format_html(f"<p>Services Agreement</p>")
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CoverCategory)
class CoverCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    
    
@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'status', 'price_per_day')
    list_filter = ('status', 'category')
    search_fields = ('name',)
    
    
    
    
class ReferralCodeInline(admin.TabularInline):
    model = ReferralCode
@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):

    list_display = ('point_of_contact', 'organization_name', 'phone', 'email')
    list_filter = ('status',)
    inlines = [
        ReferralCodeInline,
    ]
    search_fields = ('point_of_contact', 'organization_name')
    
    
    
@admin.register(OrangeZoneCover)
class OrangeZoneCoverAdmin(admin.ModelAdmin):

    list_display = ('title',)
    
    def title(self, obj):
        return format_html(f"<p>Orange Zone Cover Details</p>")
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
    
    
class MembershipPersonInline(admin.StackedInline):

    model = MembershipPerson
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):

    list_display = ('membership_id', 'status')
    inlines = [ MembershipPersonInline ]