FROM alpine:3.8
MAINTAINER titzanyic <zhangyongcun521@gmail.com>

ARG TZ='Asia/Shanghai'

RUN echo "${TZ}" > /etc/timezone
ADD frps /etc/frps
ADD frps.ini /etc/frps.ini
CMD ["/etc/frps","-c","/etc/frps.ini"]

EXPOSE 80
EXPOSE 7000
EXPOSE 7500
