from django.shortcuts import render
from .models import Auther,articale
from django.views.generic.detail import DetailView
# Create your views here.


def All(request):
    authers=Auther.objects.all()
    return render(request,'all.html',{'authers':authers})



class Detail(DetailView):
    model=Auther
    template_name='details.html'    