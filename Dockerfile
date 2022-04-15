FROM python:3.8.10-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --user -r requirements.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000