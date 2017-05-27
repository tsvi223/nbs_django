from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging, logging.config
from django.views.decorators.csrf import ensure_csrf_cookie



def check(request):
    print ('post : 1' , request.POST)

    if(request.method == 'POST'):
        try:
            fname =  request.POST['fname']
            lname =  request.POST['lname']
            context = {
                'fname' : fname,
                'lname' : lname
            }
        except Exception as e:
            context = {}
            print (e)
        print ( context)
        return render(request, 'check.html' , context)
    else:
        return render(request, 'index.html')


def index(request):
    try:
            print ('start' , request.method , request.POST['fname'])
    except Exception as e:
            print (e)
    context = {
        'chec':'todos'
    }
    return render(request, 'index.html', context)
