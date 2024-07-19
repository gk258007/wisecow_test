FROM alpine:latest


RUN apk update && \
    apk add fortune cowsay openbsd-netcat

COPY serve_wisdom.sh /usr/local/bin/serve_wisdom.sh

RUN chmod +x /usr/local/bin/serve_wisdom.sh

EXPOSE 4499

ENTRYPOINT ["/usr/local/bin/serve_wisdom.sh"]
