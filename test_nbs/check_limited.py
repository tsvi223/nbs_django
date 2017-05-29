from django.http import JsonResponse, QueryDict
from . import models

from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def do(request , action):
    print(request.data)
    if action == 'scrape-account':
        try:
            account = request.data.get('account')
            bank = request.data.get('bank')
            branch = request.data.get('branch')
            print(account , bank , branch)
            context = {
                'account_num' : account,
                'bank' : bank,
                'branch' : branch,
            }
            print(context)
        except Exception as e:
            print (e)
        res = scrapeAccounts(context)
    if action == 'scrape-personal':
        try:
            context = {
                'id' : request.data.get('id'),
            }
        except Exception as e:
            print (e)
        res = scrapePersonal(context)
    return JsonResponse({ "status" :  res})

def scrapeAccounts(account):
    print(account)
    account = models.accountLimited.objects.filter( bank = account['bank'] , account = account['account_num'] , branch = account['branch'])
    if account:
        return 'limited'
    else :
        return 'correct'

def scrapePersonal(person):
    return 'correct'

def test(request ):
    account = request.POST.get('account')
    print(account)
    return JsonResponse({ "status" :  account})
