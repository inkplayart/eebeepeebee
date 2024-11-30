FROM python:3.13.0-bookworm

RUN apt-get update -y
RUN apt-get install -y uvicorn
RUN pip install fastapi uvicorn jinja2 python-multipart

WORKDIR /eebeepeebee
COPY . . 

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2345" ]
