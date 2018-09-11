# Connect Kubernetes Cluster

gcloud container clusters get-credentials <CLUSTER_NAME> --zone <ZONE> --project <GCP_PROJECT_ID>
# Create Secret for POD to use Service Account
kubectl create secret generic cloudsql-instance-credentials --from-file=credentials.json=key.json

# DB Credentials

kubectl create secret generic cloudsql-db-credentials --from-literal=username=<DB_USER> --from-literal=password=<DB_PASSWORD>


cd ~/.kube

# kubernetes configuration file to connect cluster from inside POD
kubectl create configmap kube-config --from-file=config

# Deployment yaml, which publishes messages on pubsub

kubectl create configmap invoker-config --from-file=invoker.yaml

# Batch Jobs YAML, which acts as subscriber

kubectl create configmap batchjobs-config --from-file=batch-jobs.yaml
