from django.shortcuts import render
import pandas as pd
from . import mainfunction
# Create your views here.

def index(request):
    template_var = mainfunction.mainf()
    return render(request,"ReportCard/ReportCardTemplate.html",template_var)