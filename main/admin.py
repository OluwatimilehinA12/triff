from django.contrib import admin
from .models import Info, Verification

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['email', 'password', 'phone']
    ordering = ['email']

class VerificationAdmin(admin.ModelAdmin):
    search_fields = ['otp']
    list_display = ['otp', 'auth_code']
    ordering = ['otp']

admin.site.register(Info, InfoAdmin)
admin.site.register(Verification, VerificationAdmin)