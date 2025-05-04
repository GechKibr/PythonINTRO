from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):	
	# mysite = {
	# 'name':'Getachew kibr',
	# 'ID':'gur/02126/15',
	# }
	return render(request,'home.html',{})

def contact(request):
	# return render(request,'contact.html')
	# contacts = {
	#       'abebe':'039842934',
	#       'kebee':'0928904385',
	# }
    return render(request,'contact.html')
