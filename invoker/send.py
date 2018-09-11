#!/usr/bin/python
import pymysql
import os
import argparse
import time

from google.cloud import pubsub_v1

USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')

def get_list():
  global entries

  connection = pymysql.connect(host='127.0.0.1',user=USER,password=PASSWORD,db='<DB_NAME>')
  cur = connection.cursor()

  cur.execute("SELECT name FROM employee")

  entries = [ ','.join(names) for names in cur]
  return entries
  cur.close()
  connection.close()



def publish_messages(project, topic_name):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project, topic_name)

    for n in entries:
        data = u'Message number {}'.format(n)
        data = data.encode('utf-8')
        publisher.publish(topic_path, data=data)
        print "Message %s sent to queue" % n



get_list()
publish_messages('<GCP_PROJECT_NAME>', '<PUBSUB_TOPIC_NAME>')
