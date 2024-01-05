from django.shortcuts import render

# Create your views here.
def skills(request):
    context={'skills_active':'active'}
    return render(request,'skills.html',context)