FROM alpine:3.8
MAINTAINER titzanyic <zhangyongcun521@gmail.com>

ARG TZ='Asia/Shanghai'

RUN echo "${TZ}" > /etc/timezone
ADD godns /root/godns
CMD ["/root/godns","-c","config.json"]
