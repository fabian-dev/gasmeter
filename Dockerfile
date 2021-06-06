FROM python:3.9-buster

RUN apt-get update && apt-get install -y "wait-for-it"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py .

CMD ["wait-for-it", "influxdb:8086", "-t", "60", "--", "python", "run.py"]