from django.shortcuts import render,HttpResponse
def fun(request):
    return HttpResponse('<h1>Hello everyone </h1>')

def about(request):
    return render(request,'home.html')
