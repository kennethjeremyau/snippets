APP_NAME=example-app

build:
	docker build --rm -t $(APP_NAME) .
run:
	docker run -it --rm $(APP_NAME)
up: build run

.PHONY: build, run, up
