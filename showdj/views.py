from django.shortcuts import render

# Create your views here.

def show(request):
    datas={

    }
    return render(request,'pages/show/show.html')
    