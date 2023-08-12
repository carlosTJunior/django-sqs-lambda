FROM python:3.9.9

WORKDIR /api
COPY . /api/
RUN pip install --upgrade pip && pip install -r requirements.txt
