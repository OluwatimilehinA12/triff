from django.db import models

from django.core.exceptions import ValidationError

# Create your models here.

class Info(models.Model):
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.email if self.email else self.phone if self.phone else "No contact info" 
    

class Verification(models.Model):
    otp = models.CharField(max_length=6, blank=True, null=True)
    auth_code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.otp and not self.auth_code:
            raise ValidationError("Either OTP or auth_code must be provided")

    def save(self, *args, **kwargs):
        self.full_clean()  # Runs model validation
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Verification(OTP: {self.otp}, Auth Code: {self.auth_code})"