FROM python:3.8.3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
CMD [ "sh", "./startup.sh" ]