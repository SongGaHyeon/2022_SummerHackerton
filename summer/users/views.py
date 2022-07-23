from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request, user)
        else: print("실패")
    return render(request, "users/login.html")