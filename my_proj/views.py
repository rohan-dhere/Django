from django.http import HttpResponse
from django.shortcuts import render #to render entire page

def home(request): #home.html page function
    return render(request,'home.html')
def addition(request): #addition.html function
    return render(request,'addition.html')

 #get num1 & num2 from addition.html and add them
def btnResult(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    my_sum  = (val1) + (val2)
    return render(request,'result.html', {'ans':my_sum}) #return sum to result.html