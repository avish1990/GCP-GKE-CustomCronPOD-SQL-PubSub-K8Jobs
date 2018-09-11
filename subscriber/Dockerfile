FROM ubuntu:latest
ADD subscriber.py Jelly/subscriber.py
RUN apt-get update && apt-get install -y vim mysql-server curl python python-pip && pip install --upgrade pymysql google-api-python-client google-cloud google-cloud-pubsub
CMD /Jelly/subscriber.py 
