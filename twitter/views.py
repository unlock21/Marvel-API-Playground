from django.http import JsonResponse, HttpResponse
from django.template import loader

from .models import tweet

def index(request):
    query = request.GET.get('q', 'NOT_PROVIDED')
    if query != 'NOT_PROVIDED':
        searchTweets = tweet.objects.filter(body__contains=query)
    else:
        searchTweets = []
    allTweets = tweet.objects.all()
    template = loader.get_template('twitter/index.html')
    context = {
        'allTweets': allTweets,
        'searchTweets': searchTweets,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    query = request.GET.get('q', '')
    searchTweets = tweet.objects.filter(body__contains=query)
    return JsonResponse(list(searchTweets.values()), safe=False)