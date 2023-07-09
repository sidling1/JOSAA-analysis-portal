from django.shortcuts import redirect, render
from django.http import HttpResponse

import json
# Create your views here.

def index(request):
    return redirect('http://localhost:8000/home/')