from django.http import HttpResponse, JsonResponse
from django.template import loader

from marvel.models import Character, Comic

app_name = 'marvel'
def index(request):
    query = request.GET.get('q', '')
    searchCharacters = []
    if query != '':
        searchCharacters = Character.objects.filter(name__contains=query).select_related()
    template = loader.get_template('marvel/index.html')
    context = {
         # All characters and Comics
        'allCharacters': Character.objects.select_related(),
        'searchCharacters': searchCharacters,
        'query': query,
    }
    return HttpResponse(template.render(context, request))

def characters(request):
    return JsonResponse(list(Character.objects.values()), safe=False)

# def characterSearch(request):
#     query = request.GET.get('q', '')
#     if (query == ''): return JsonResponse([])
#     characters = Character.objects.filter(name__contains=query)
#     result = []
#     for character in characters:
#         result.append(Comic.objects.filter(character=character).values())
#     return JsonResponse(list(result), safe=False)

def comics(request):
    return JsonResponse(list(Comic.objects.values()), safe=False)

# def comicsSearch(request):
#     query = request.GET.get('q', '')
#     if (query == ''): return JsonResponse([])
#     comics = Comic.objects.filter(name__contains=query).select_related()
#     # characters = comics.character_set.all()
#     print(characters)
#     return JsonResponse(list(comics.values()), safe=False)