FROM redis:5.0.6-alpine3.10

WORKDIR /app
COPY sentinel.conf .

CMD ["redis-server", "/app/sentinel.conf", "--sentinel"]
