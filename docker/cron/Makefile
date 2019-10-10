SERVICE=cron

build: remove
	docker-compose build

down:
	docker-compose down

shell:
	docker-compose exec -it $(SERVICE) /bin/sh

up:
	docker-compose up $(SERVICE)

.DEFAULT_GOAL: build
.PHONY: build down shell up
