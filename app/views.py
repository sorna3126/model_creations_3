from django.shortcuts import render
from app.models import *
# Create your views here.

def display_country(request):

    QLCO =Country.objects.all()

    d={'Code':QLCO}

    return render(request,'display_country.html',d)


def display_capital(request):

    QLCAO=Capital.objects.all()

    d={'Capitals':QLCAO}
    
    return render(request,'display_capital.html',d)