from twitter.models import tweet

def bodyContains(query):
    return tweet.objects.filter(body__contains=query)