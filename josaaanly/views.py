from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from django.db.models import IntegerField
from django.db.models.functions import Cast

# Create your views here.


def home(request):
    return render(request,'josaaanly/home.html',{'rank':0})

def graph(request):
    if request.method == 'POST':
        rank = request.POST.get('your_rank')
    
    return render(request,'josaaanly/graph.html',{'rank':rank})

def plotgraph(request):
    data = Data.objects.all()

    if request.method == 'POST':
        rank = int(request.POST.get('rank'))
        sel_opt = request.POST.get('graph-type')

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

def InstituteDetails(request):

    if request.method == 'POST':
        insti = request.POST.get('insti')

    return render(request,"josaaanly/Institute/InstituteDetails.html",{'Institute':insti})