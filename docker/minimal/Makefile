APP_NAME=example-app

.PHONY: build, run, up

build:
	docker build --rm -t $(APP_NAME) .

run:
	docker run -it --rm $(APP_NAME)

up: build run
