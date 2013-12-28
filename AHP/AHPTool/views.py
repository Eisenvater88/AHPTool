from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from AHPTool.models import Dimension
from AHPTool.models import Rating
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from AHPTool.ResultGen import ResultGen
import datetime
import hashlib

# Create your views here.
def index(request):
    request.session['key'] = str(datetime.datetime.now()).split('.')[0]
    if request.method == 'GET':
        dimensions = Dimension.objects.all()
        list =[]
        i = 0
        while (len(dimensions)>i):
            for val in dimensions[i:]:
                if (dimensions[i]!= val):
                    list.append((dimensions[i], val))
            i+=1
        template = loader.get_template('AHPTool/index.html')

        context = RequestContext(request, {'list':list,})
    #out = ', '.join([p.name for p in dimensions])
        return HttpResponse(template.render(context))

@csrf_exempt
def save(request):
    s_key = hashlib.sha224(request.session['key']).hexdigest()
    print s_key
    if request.method == 'GET':
        dimensions = Dimension.objects.all()
        list =[]
        i = 0
        k = 0
        while (len(dimensions)>i):
            for val in dimensions[i:]:
                if (dimensions[i]!= val):
                    #print dimensions[i]
                    list.append((dimensions[i], val, request.GET.dict().get(str(k)), s_key)) #k is the real iterator 
                    k+=1
            i+=1
        for t in list:
            d1,d2,v,k = t
            v = int(v)
            if v > 0:
                d1,d2 = d2,d1
            elif v < 0:
                v = v*(-1)
            v+=1    
            r =  Rating(Dim1 = d1, Dim2 = d2, sessionkey=k, rating = v)
            r.save()
            
        return HttpResponse()

def generateResult(request):
    res = ResultGen()
    final_vector, summe = res.getResult()
    template = loader.get_template('AHPTool/result.html')
    context = RequestContext(request, {'list':final_vector,'sum':summe})
    return HttpResponse(template.render(context))
    
    