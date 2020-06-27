## Getting Started

### Local Run

    git clone https://github.com/unlock21/Marvel-API-Playground.git

    export DJANGO_PRIVATE_KEY="<LONG STRING>"
    export MARVEL_PUBLIC_KEY="<MARVEL PUBLIC KEY>"
    export MARVEL_PRIVATE_KEY="<MARVEL PRIVATE KEY>"
    pip install -r requirements.txt
    sh ./startup.sh

### Using Docker

    docker run -d -e DJANGO_PRIVATE_KEY=<LONG STRING> -e MARVEL_PUBLIC_KEY=<MARVEL PUBLIC KEY> -e MARVEL_PRIVATE_KEY=<MARVEL PRIVATE KEY> -p 80:80 14ecassidy/ues_demo:latest

~~### Using Deployed Version

~~*Container in Azure*

~~Navigate to [http://ues-demo-django.eastus.azurecontainer.io/](http://ues-demo-django.eastus.azurecontainer.io/)

## Project Layout

### Marvel

URLS:

    # Landing page for search
    path('', views.index, name='index'),
    # GET characters stored in database
    path('api/marvel/characters', views.characters, name="characters"),
    # GET comics stored in database
    path('api/marvel/comics', views.comics, name="comics"),

VIEWS:

    # Returns index.html template
    index
    # Returns JSON array with all characters
    characters
    # Returns JSON array with all comics
    comics

### Marvel_API

How to Use:

    python ./manage.py runscript importApiData
