#!/bin/bash

# Ensure k8s is running.
minikube status || minikube start

# Install RabbitMQ Cluster Operator
# This is a k8s plugin which allows us to use the rabbitmqcluster kind.
kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml"

# Create the RabbitMQ servers.
kubectl apply -f deployment.yaml

# Display GUI credentials
echo GUI Username:
kubectl get secret rabbitmq-example-default-user -o jsonpath="{.data.username}" | base64 --decode
echo
echo
echo GUI Password:
kubectl get secret rabbitmq-example-default-user -o jsonpath="{.data.password}" | base64 --decode

