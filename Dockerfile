FROM python:3.9-slim
COPY . /oopt-gnpy-api
WORKDIR /oopt-gnpy-api
RUN apt update; apt install -y git
RUN pip install .
RUN mkdir -p /opt/application/oopt-gnpy/autodesign
CMD [ "python", "./samples/rest_example.py" ]