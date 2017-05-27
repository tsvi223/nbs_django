from django.http import JsonResponse
import requests

def do(request):

    r = requests.get('http://www.google.com')
    print (r.text)
    return JsonResponse({'foo': 'ffd' })
