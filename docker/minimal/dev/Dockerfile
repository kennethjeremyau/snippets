FROM python

RUN apt-get update && apt-get install -y \
    black \
    build-essential \
    curl \
    docker.io \
    docker-compose \
    git \
    vim \
    && apt-get clean

CMD ["bash", "-c", "trap 'exit 0' SIGTERM; while true; do sleep 1; done"]
