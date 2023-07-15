FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /cargo
COPY requirements.txt /cargo/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /cargo/
EXPOSE 8000