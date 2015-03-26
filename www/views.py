#-*-coding:utf8;-*-
from django.http import HttpResponse, Http404
from django.conf import settings
from tenjin_shortcuts import render_to_response 
from name.models import Name
from name.func import chinese_to_gr


def index(request, template_name="www/index.html"):                            
    rt = render_to_response(template_name, {                                   
    }, context_instance=request)                                               
    return HttpResponse(rt)

def ename(request, name=None,  template_name="www/ename.html"):                            
    try:                                                                       
        n = Name.objects.select_related().get(name=name)                  
    except Name.DoesNotExist:                                               
        raise Http404 
    rt = render_to_response(template_name, {                                   
        'name':n,
    }, context_instance=request)                                               
    return HttpResponse(rt)

def plan(request, name=None, gender=None,  template_name="www/plan.html"):                            
    if len(name) > 2 and name[0:2] in settings.FUXING_LIST:
        n = name[2:]
    else:
        n = name[1:]
    gr = chinese_to_gr(n)
    print gr
    rt = render_to_response(template_name, {                                   
        'name':name,
        'gender':gender,
    }, context_instance=request)                                               
    return HttpResponse(rt)

def query(request, template_name="www/request.html"):
    rt = render_to_response(template_name, {                                   
    }, context_instance=request)                                               
    return HttpResponse(rt)

