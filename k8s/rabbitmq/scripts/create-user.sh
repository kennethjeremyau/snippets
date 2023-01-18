#!/bin/bash

echo "Username: "
read username

echo "Password: "
read password

kubectl exec rabbitmq-example-server-0 -c rabbitmq -- rabbitmqctl add_user "$username" "$password"

kubectl exec rabbitmq-example-server-0 -c rabbitmq -- rabbitmqctl set_user_tags "$username" administrator

kubectl exec rabbitmq-example-server-0 -c rabbitmq -- rabbitmqctl set_permissions -p / "$username" ".*" ".*" ".*"
