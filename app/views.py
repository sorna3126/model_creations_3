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

def insert_country(request):

    cc=input('enter the code: ')
    cn=input('enter country name: ')

    NCO=Country.objects.get_or_create(Country_Code=cc,Country_Name=cn)[0]
    NCO.save()
    

    QLCO =Country.objects.all()

    d={'Code':QLCO}

    return render(request,'display_country.html',d)

def insert_capital(request):
    cc=input('enter the code: ')
    Can=input('enter the capital name: ')
    cur=input('enter the currency: ')

    CO=Country.objects.get(Country_Code=cc)

    NCAO=Capital.objects.get_or_create(Country_Code=CO,Capital_Name=Can,Currency=cur)[0]
    NCAO.save()

    QLCAO=Capital.objects.all()

    d={'Capitals':QLCAO}



    return render(request,'display_capital.html',d)
