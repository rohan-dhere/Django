from django.http import HttpResponse
from django.shortcuts import render #to render entire page
from .models import blogs

# Create your views here.
def index(request):
    my_blog_list = blogs.objects.all() #fetching data from db
    return render(request,'index.html',{'my_blog_list': my_blog_list}) #return sum to result.html