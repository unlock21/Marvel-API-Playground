from django.http import HttpResponse, JsonResponse
from django.template import loader

from marvel_api import api

from marvel.models import Character, Comic

app_name = 'marvel'
def index(request):
    # api.getCharacters() # Load from API
    template = loader.get_template('marvel/index.html')
    context = {
        'allCharacters':Character.objects.all()
    }
    return HttpResponse(template.render(context, request))

def characters(request):
    return JsonResponse(list(Character.objects.values()), safe=False)

def comics(request):
    return JsonResponse(list(Comic.objects.values()), safe=False)

def comicsSearch(request):
    query = request.GET.get('q', '')
    if (query == ''): return JsonResponse([])
    return JsonResponse(list(Comic.objects.filter(name__contains=query).values()), safe=False)