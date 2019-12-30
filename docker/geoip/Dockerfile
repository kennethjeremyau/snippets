FROM golang:1.13.5-alpine3.11
RUN apk add --no-cache make
WORKDIR /root
COPY geoipupdate-4.1.5.tar.gz .
RUN tar xf geoipupdate-4.1.5.tar.gz \
    && cd geoipupdate-4.1.5 \
    && make build/geoipupdate

FROM alpine:3.11.2
COPY --from=0 /root/geoipupdate-4.1.5/build/geoipupdate /opt/maxmind/geoipupdate
COPY GeoIP.conf /usr/local/etc/GeoIP.conf
RUN mkdir -p /usr/local/share/GeoIP \
    && echo '0 0 * * 1 /opt/maxmind/geoipupdate' >> /var/spool/cron/crontabs/root
CMD /opt/maxmind/geoipupdate && /usr/sbin/crond -f
