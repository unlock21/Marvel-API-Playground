from django.http import JsonResponse, HttpResponse
from django.template import loader

from .api.search import bodyContains
from .api.get import getAll

def index(request):
    query = request.GET.get('q', 'NOT_PROVIDED')
    if query != 'NOT_PROVIDED':
        searchTweets = bodyContains(query)
    else:
        searchTweets = []
    template = loader.get_template('twitter/index.html')
    context = {
        'allTweets': getAll(),
        'searchTweets': searchTweets,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    query = request.GET.get('q', '')
    return JsonResponse(list(bodyContains(query).values()), safe=False)