from django.shortcuts import render
from .models import Blog
# Create your views here.
def modal(request):
    blogs = Blog.objects
    return render(request, 'modal/modal.html', {'blogs':blogs})
