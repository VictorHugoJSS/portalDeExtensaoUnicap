from django.shortcuts import render

# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'admin-cards.html')

def AdminPageView(request):
    return render(request, 'admin-cards.html')

def Create(request):
    return render(request, 'create.html')

def LoginView(request):
    return render(request, 'login.html')

