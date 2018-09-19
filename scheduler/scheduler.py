#!/usr/bin/python
#!/usr/bin/python
from os import path

import yaml

from kubernetes import client, config

config.load_kube_config()

def create_deploy():

    with open(path.join(path.dirname(__file__), "/invoker-config/invoker.yaml")) as f:
        dep = yaml.load(f)
        k8s_beta = client.AppsV1Api()
        resp = k8s_beta.create_namespaced_deployment(
            body=dep, namespace="default")
        print("Deployment created. status='%s'" % str(resp.status))

def create_job():

    with open(path.join(path.dirname(__file__), "/subscriber-config/subscriber.yaml")) as f:
        dep = yaml.load(f)
        k8s_beta = client.BatchV1Api()
        resp = k8s_beta.create_namespaced_job(
            body=dep, namespace="default")
        print("Batch Job created. status='%s'" % str(resp.status))


def delete_deploy():

    body = client.V1DeleteOptions()
    k8s_beta = client.AppsV1Api()
    name = "cyb-invoke"
    namespace = "default"
    resp = k8s_beta.delete_namespaced_deployment(
        name, namespace, body)
    print("Deployment deleted. status='%s'" % str(resp.status))

def delete_job():

    body = client.V1DeleteOptions()
    k8s_beta = client.BatchV1Api()
    pod_api = client.CoreV1Api()
    name = "cyb"
    name_job = "cyb-sub"
    namespace = "default"

    pod_list = pod_api.list_pod_for_all_namespaces(label_selector="app={}".format(name), pretty=True)



    for item in pod_list.items:
        pod_name = item.metadata.name
        print("Found '{}', deleting...".format(pod_name))
        pod_resp = pod_api.delete_namespaced_pod(pod_name, namespace, body)

    resp = k8s_beta.delete_namespaced_job(name_job, namespace, body)
    print("Jobs deleted. status='%s'" % str(resp.status))

try:
  delete_job()
  delete_deploy()
  create_deploy()
  create_job()
except:
  try:
    delete_deploy()
    create_deploy()
    create_job()
  except:
    create_deploy()
    create_job()
