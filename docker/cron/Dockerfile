FROM alpine

WORKDIR /app
COPY . /app
RUN cp crontab /etc/crontabs/root
CMD /app/cron-entrypoint.sh
