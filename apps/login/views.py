from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
	return render(request, "login/index.html")

def register(request):
	print("herlllasf")
	kwargs = request.POST
	reg = User.userManager.register(**kwargs)
	print reg
	print "*"*500
	print kwargs
	return redirect('/')
