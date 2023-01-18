build:
	docker build -t rabbitmq-pika-client . \
		&& docker tag rabbitmq-pika-client localhost:5000/rabbitmq-pika-client \
		&& docker push localhost:5000/rabbitmq-pika-client
build-registry:
	docker run -d -p 5000:5000 --restart=always --name registry registry:2
up: build
	kubectl apply -f deployment.yaml
