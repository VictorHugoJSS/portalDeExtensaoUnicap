from django.shortcuts import render

# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'base.html')

def AdminPageView(request):
    return render(request, 'admin-base.html')