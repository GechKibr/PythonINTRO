from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request,*args,**kwargs):
	print(args,kwargs)
	print(request)
	# return HttpResponse()
	return render(request,'home.html')

def contact(request,*args,**kwargs):
    # return HttpResponse('contact page ')	
     return render(request,'contact.html')