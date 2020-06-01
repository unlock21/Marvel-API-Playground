python3 ./manage.py migrate
python3 ./manage.py runscript importApiData & # Make this async so the webserver can take requests while api data is loaded
python3 ./manage.py runserver 0.0.0.0:80