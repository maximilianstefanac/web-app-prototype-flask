FROM python:3.8-buster
ADD . /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y libgeos-c1v5
RUN pip install -r requirements.txt
CMD ["python", "app.py"]