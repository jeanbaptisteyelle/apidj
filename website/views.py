from django.shortcuts import render

# Create your views here.
def index(request):
    datas={

    }
    return render(request,'pages/website/index.html')
    