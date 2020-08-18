#from django.http import HttpResponse
from django.shortcuts import render
def home (request):
	#return HttpResponse('HEllo acme')
	return render(request,'pages/home.html')

def handler404(request, exception):
	return render(request, 'errors/404.html', {'error':exception}, status=404)

def handler500(request, exception=None):
	return render(request, 'errors/500.html', {'error':exception}, status=500)
	#handler 500