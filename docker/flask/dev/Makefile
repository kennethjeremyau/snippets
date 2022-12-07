.PHONY: build
build:
	docker-compose build

.PHONY: up
up: build
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.DEFAULT_GOAL: build
