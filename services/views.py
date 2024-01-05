from django.shortcuts import render

# Create your views here.
def services(request):
    context={'services_active':'active'}
    return render(request,'services.html',context)