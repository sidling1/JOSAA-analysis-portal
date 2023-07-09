from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from django.db.models import IntegerField
from django.db.models.functions import Cast
import json
# Create your views here.


def home(request,valid=True):
    return render(request,'josaaanly/home.html',{'rank':1,'valid':valid})

def graph(request):
    if request.method == 'POST':
        rank = request.POST.get('your_rank')
    
    if rank.isnumeric():
        rank = int(rank)
    else:
        print('Put in a number')
        return home(request,False)

    if rank <= 0:
        print('value has to be greater than 0')
        return home(request,False)
    if rank > 1000000:
        print('Put in your real rank bruh !')
        return home(request,False)

    return plotgraph(request,rank)

def plotgraph(request,rank):
    data = Data.objects.all()

    # if request.method == 'POST':
    #     rank = int(request.POST.get('rank'))
        # sel_opt = request.POST.get('graph-type')

    data = Data.objects\
            .annotate(OR=Cast('OpeningRank',output_field=IntegerField()))\
            .annotate(CR=Cast('ClosingRank',output_field=IntegerField()))\
            .filter(OR__lte=rank)\
            .filter(CR__gte=rank)\
            .filter(SeatType='OPEN')\
            .filter(Year="2022")\
            .filter(Round = 1)\
            .filter(DualDeg = False)\
            .order_by('OR')

    return render(request,"josaaanly/plotgraph.html",{'data':data,'rank':rank})

def selectInstitute(request):
    data = Data.objects.values('Institute').distinct()

    return render(request,"josaaanly/Institute/selectInstitute.html",{'data':data})

def selectBranch(request):
    data = Data.objects.values('Programme').distinct()

    return render(request,"josaaanly/Institute/selectBranch.html",{'data':data})

#Just for the institutes
def InstituteDetails(request):

    if request.method == 'POST':
        insti = request.POST.get('insti')
        seat = request.POST.get('seat')
    data = Data.objects.filter(Institute=insti,SeatType=seat,Round = 1,Year = 2022,Gender='Gender-Neutral').order_by('Programme')
    
    x_values = list(data.values('Programme'))

    y_values = list(data.values('ClosingRank'))

    return render(request,"josaaanly/Institute/InstituteDetails.html",{'insti':insti,'x_values':x_values,'y_values':y_values,'seat':seat})


def BranchDetails(request):

    if request.method == 'POST':
        branch = request.POST.get('branch')
        seat = request.POST.get('seat')
    data = Data.objects.filter(Programme=branch,SeatType=seat,Round = 1,Year = 2022,Gender='Gender-Neutral').order_by('Institute')
    
    x_values = list(data.values('Institute'))

    y_values = list(data.values('ClosingRank'))

    return render(request,"josaaanly/Institute/BranchDetails.html",{'branch':branch,'x_values':x_values,'y_values':y_values,'seat':seat})

