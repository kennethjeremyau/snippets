FROM alpine:latest

RUN apk add --no-cache netcat-openbsd
WORKDIR /app
COPY entrypoint.sh .

CMD ["/app/entrypoint.sh"]
