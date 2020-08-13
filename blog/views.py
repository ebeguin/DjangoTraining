from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def index(request):
	posts= Post.objects.all()
	return render(request,'blog/index.html',{'posts':posts})

def show(request, id):
	post = get_object_or_404(Post, pk=id)
	return render (request,'blog/show.html', {'post':post})