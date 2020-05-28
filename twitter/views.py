from django.http import JsonResponse, HttpResponse
from django.template import loader

from .models import tweet

def index(request):
    # TODO: SIMPLIFY FORM
    query = request.POST.get('q', '')
    searchTweets = tweet.objects.filter(body__contains=query)
    tweets = tweet.objects.all()
    template = loader.get_template('twitter/index.html')
    context = {
        'tweets': tweets,
        'searchTweets': searchTweets,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    query = request.GET.get('q', '')
    tweets = tweet.objects.filter(body__contains=query)
    return JsonResponse(list(tweets.values()), safe=False)