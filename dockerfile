FROM python:3.10

WORKDIR /root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD python ghost_task/manage.py runserver 0.0.0.0:8000 