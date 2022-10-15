APP_NAME=example-app

.PHONY: build
build:
	docker build --rm -t $(APP_NAME) .

.PHONY: run
run:
	docker run -it --rm $(APP_NAME)

.PHONY: up
up: build run
