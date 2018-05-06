SERVICE=cron

build: remove
	docker-compose build

enter:
	docker-compose exec $(SERVICE) /bin/sh -l

remove:
	docker-compose rm -f $(SERVICE)

run:
	docker-compose up $(SERVICE)

.DEFAULT_GOAL: build
.PHONY: build, enter, remove, run
