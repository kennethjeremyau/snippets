# RabbitMQ on Kubernetes

## Installation (Minikube on OSX)
1. Start Docker for Mac.
1. `./install.sh`
1. (Optional) `minikube tunnel` in another terminal to access the GUI at localhost:15672.

# Manual testing (Minikube on OSX)
1. `eval $(minikube docker-env)`
1. Navigate to the appropriate client directory.
1. `make up`
1. `kubectl get pods`
1. `kubectl exec -it <POD_NAME> -- /bin/bash`
1. When finished: `eval $(minikube docker-env -u)`
