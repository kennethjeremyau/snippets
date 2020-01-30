FROM redis:5.0.6-alpine3.10

WORKDIR /app
COPY redis.conf .

CMD ["redis-server", "/app/redis.conf"]
