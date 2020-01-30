build:
	docker-compose build
down:
	docker-compose down
up:
	docker-compose up -d --scale redis=6

.DEFAULT_GOAL := up
.PHONY: build up down
