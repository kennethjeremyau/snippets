build:
	docker build -t nginx-test .
down:
	docker stop nginx-test
up:
	docker run -dit --rm --name nginx-test -p 9090:80 nginx-test
