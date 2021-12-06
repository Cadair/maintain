# base image
FROM python:3.10

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -U pip setuptools wheel && pip install -r requirements.txt
COPY . .

# port where the Django app runs
EXPOSE 8000
CMD python manage.py runserver
