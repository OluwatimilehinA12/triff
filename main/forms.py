from django import forms
from django.core.exceptions import ValidationError
from .models import Info, Verification

class InfoForm(forms.ModelForm):
    email_or_phone = forms.CharField(required=False)  # Add this field

    class Meta:
        model = Info
        fields = ['email_or_phone', 'password']
        widgets = {
            'password': forms.TextInput(attrs={'type': 'text'})  # Set the type to text
        }

    def clean(self):
        cleaned_data = super().clean()
        email_or_phone = cleaned_data.get('email_or_phone')
        password = cleaned_data.get('password')
        
        if not email_or_phone:
            raise forms.ValidationError("Either email or phone must be provided.")
        if not password:
            raise forms.ValidationError("Password must be provided.")
        
        return cleaned_data
    


class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['otp', 'auth_code']
        widgets = {
            'otp': forms.TextInput(attrs={
                'placeholder': 'Enter OTP',
                'maxlength': '6',
                'class': 'form-control'
            }),
            'auth_code': forms.TextInput(attrs={
                'placeholder': 'Enter Authentication Code',
                'maxlength': '6',
                'class': 'form-control'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        otp = cleaned_data.get('otp')
        auth_code = cleaned_data.get('auth_code')
        
        # Require at least one field to be filled
        if not otp and not auth_code:
            raise ValidationError("Please enter either OTP or Authentication Code")
        
        return cleaned_data