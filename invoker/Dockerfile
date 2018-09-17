FROM ubuntu:latest
ADD invoker.py invoker/invoker.py 
RUN apt-get update && apt-get install -y vim mysql-server curl python python-pip && pip install --upgrade pymysql google-api-python-client google-cloud google-cloud-pubsub
CMD touch /var/log/invoker.log && /invoker/invoker.py >> /var/log/invoker.log 2>&1 && tail -f /var/log/invoker.log
