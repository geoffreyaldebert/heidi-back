
FROM python:3.9

COPY ./heidi-back /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "app.py" ] 
