FROM alpine:3.12.0

RUN apk add docker-compose \
    --no-cache \
    --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

WORKDIR /app

COPY crontab /etc/crontabs/root
COPY . .

CMD ["/usr/sbin/crond", "-f"]
