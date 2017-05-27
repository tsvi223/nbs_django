from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging, logging.config


from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    context = {
        'chec':'todos'
    }
    return render(request, 'index.html', context)

@ensure_csrf_cookie
def check(request):
     print ('Goodbye, cruel world!')
    # if(request.method == 'POST'):
    #     context = {
    #         fname : request.POST['fname'],
    #         lname : request.POST['lname']
    #     }
    #     return render(request, 'check.html' , context)
    # else:
    #     return render(request, 'index.html')
