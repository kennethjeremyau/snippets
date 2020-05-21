FROM alpine

RUN apk add --no-cache aws-cli \
        --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community \
    && aws ec2 describe-instances

CMD ["tail", "-f", "/dev/null"]
