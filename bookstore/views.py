from django.shortcuts import render,redirect
from contactenquiry.models import contactEnquiry
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.core.mail import send_mail



from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator

def home(request):
    return render(request,"indext.html")
def about(request):
    return render(request,"about.html")
def booklib(request):
    return render(request,"booklib.html")
def contact(request):
    return render(request,"contect.html")
def saveEnquiry(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        en = contactEnquiry(name=name,email=email,message=message)
        en.save()
    return HttpResponseRedirect("/thankyou") 
    return render(request,"contect.html")
def thankyou(request):
    return render(request,"thankyou.html")
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create user instance
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # set password using the set_password method
            user.save()

            # Show success message and redirect to login page
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with your form.")
    else:
        form = RegisterForm()

    return render(request, "sign.html", {"form": form})
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # If you want to authenticate by email, make sure you've created a custom backend (explained below)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Log the user in
            auth_login(request, user)
            return redirect("home")  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid login credentials. Please try again.")

    return render(request, "login.html")

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=email)
                # Send password reset email
                subject = 'Password Reset Request'
                message = f"To reset your password, click the link below:\n"
                message += f"{request.build_absolute_uri('/reset/password/')}"
                send_mail('Password_reset', '3456', 'tusharpaliwal.mca23@acropolis.in', ['daswanikhushbu5@gmail.com'])

                messages.success(request, 'Password reset instructions sent successfully!')
                return render(request, 'password_reset.html', {'form': form})
            except User.DoesNotExist:
                messages.error(request, 'Email address not found in our records.')

    else:
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form})