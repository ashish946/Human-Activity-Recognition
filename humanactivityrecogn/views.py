from django.shortcuts import render
import HAR

def index(request):
    return render(request,'index.html')

def result(request):
    n=request.GET['num']
    b=HAR.model(n)
    print(b)
    return render(request,'result.html',{'res':b})
