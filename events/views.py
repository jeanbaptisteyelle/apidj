from django.shortcuts import render

# Create your views here.
def dj(request):
    datas={

    }
    return render(request,'pages/events/dj.html')
    
def events(request):
    datas={

    }
    return render(request,'pages/events/events.html')

def single(request):
    datas={

    }
    return render(request,'pages/events/single.html')
    


def about(request):
    datas={

    }
    return render(request,'pages/events/about.html')

def contact(request):
    datas={

    }
    return render(request,'pages/events/contact.html')
    