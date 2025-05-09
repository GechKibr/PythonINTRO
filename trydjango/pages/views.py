from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request,*args,**kwargs):	
	mysite = {}
	return render(request,'home.html',mysite)
	# return HttpResponse('hello world ')
def contact(request,*args,**kwargs):
	# contacts = {}
    return render(request,'contact.html',{})
    # return HttpResponse('Hello world')
