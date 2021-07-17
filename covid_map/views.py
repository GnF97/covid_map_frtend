from django.shortcuts import render

from .models import County
import numpy as np

a = County.objects.values('patient_count')

# Create your views here.
def index(request):
    return render(request, "County/index.html",{
        "Counties" : County.objects.all(),
        "Sumup" : sum([list(a[i].values())[0] for i in range(len(a))])
    })

def county(request, county_idc):
    # idc = County.objects.get(pk=county_idc)
    return render(request, "County/county.html",{
        "County" : County.objects.filter(idc = county_idc)[0]
        })
