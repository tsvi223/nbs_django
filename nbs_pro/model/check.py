from django.http import JsonResponse
import requests
from promise import Promise

def do(request):
    r = requests.get('http://www.google.com')
    print (r.text)
    return JsonResponse({'foo': 'ffd' })



def scrape(request ,action ):
    print('enter' , action)
    res = {}
    context = {}
    if 'scrape-account':
        try:
            account = request.POST.get('account')
            bank = request.POST.get('bank')
            branch = request.POST.get('branch')
            context = {
                'account' : account,
                'bank' : bank,
                'branch' : branch,
            }
        except Exception as e:
            print (e)
        res = scrapeAccounts(context)
    if 'scrape-personal':
        try:
            context = {
                'id' : request.POST.get('id'),
            }
        except Exception as e:
            print (e)
        res = scrapePersonal(context)
    return JsonResponse({ "" :  res})



def scrapeAccounts(context):
    return r.text


def scrapePersonal(context ):
    promise = Promise()
    r = requests.get('http://www.google.com')
    return r.text
