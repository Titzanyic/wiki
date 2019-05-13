FROM alpine:3.8
MAINTAINER titzanyic <zhangyongcun521@gmail.com>

ARG TZ='Asia/Shanghai'

RUN echo "${TZ}" > /etc/timezone
ADD frpc /etc/frpc
CMD ["/etc/frpc","-c","/etc/frpc.ini"]
