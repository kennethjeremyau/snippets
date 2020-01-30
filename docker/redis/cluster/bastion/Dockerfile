FROM redis:5.0.6-alpine3.10

RUN apk add --no-cache bind-tools
WORKDIR /app
COPY entrypoint.sh .

CMD ["/app/entrypoint.sh"]
