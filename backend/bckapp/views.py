from django.shortcuts import render,HttpResponse

# Create your views here.
def main(request):
    return render(request, 'main.html')

def user_login(request):
    return render(request, 'userlogin.html')

def register(request):
    return render(request, 'register.html')

def org_login(request):
    return render(request, 'org-login.html')

def sign_up(request):
  return render(request, 'sign_up-01.html')

def sign_up02(request): 
     return render(request, 'sign_up-02.html')

def sign_up03(request):
    return render(request, 'sign_up-03 .html')   