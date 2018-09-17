FROM ubuntu:latest
ADD scheduler.py scheduler/scheduler.py 
COPY scheduler-cron /etc/cron.d/scheduler-cron
#COPY config /root/.kube/
RUN apt-get update && apt-get install -y cron vim curl python python-pip && pip install --upgrade kubernetes && touch /var/log/cron.log && service cron start && chmod 0644 /etc/cron.d/scheduler-cron && crontab /etc/cron.d/scheduler-cron
CMD printenv >> /etc/environment && cron && cp /cluster-config /root/.kube/config && tail -f /var/log/cron.log
