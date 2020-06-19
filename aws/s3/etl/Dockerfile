FROM alpine:3.12.0

RUN apk add aws-cli file jq vim \
    --no-cache \
    --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

WORKDIR /app

COPY . .

CMD ["/app/process.sh", "gdpr", "firehose.gfycat.com"]
