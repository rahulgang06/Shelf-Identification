# Dockerfile
FROM python:3.8

WORKDIR /apps

COPY requirements.txt /apps/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /apps/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
