FROM ubuntu:latest
ADD trigger.py Jelly/trigger.py 
COPY jellycron /etc/cron.d/jellycron
COPY config /root/.kube/
RUN apt-get update && apt-get install -y cron vim curl python python-pip && pip install --upgrade kubernetes && touch /var/log/cron.log && service cron start && chmod 0644 /etc/cron.d/jellycron && crontab /etc/cron.d/jellycron
CMD printenv >> /etc/environment && cron && tail -f /var/log/cron.log
