from twitter.models import tweet

def getAll():
    return tweet.objects.all()