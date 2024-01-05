from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    context={'home_active':'active'}
    return render(request,"home.html",context)

def contact(request):
    context={'contact_active':'active'}
    return render(request,'contact.html',context)
