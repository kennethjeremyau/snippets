FROM alpine

WORKDIR /app
COPY . .

RUN apk add --update python py-pip
RUN apk add --virtual build-dependencies python-dev build-base \
    && pip install -r requirements.txt \
    && apk del build-dependencies \
    && rm -rf /var/cache/apk/*

CMD ["/app/main.sh"]
