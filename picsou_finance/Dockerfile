FROM ghcr.io/cloeille/picsou-finance/bourso-auth:latest AS bourso

FROM ghcr.io/cloeille/picsou-finance:latest

USER root

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
       postgresql python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY --from=bourso /app /opt/bourso
RUN pip3 install --no-cache-dir -r /opt/bourso/requirements.txt

COPY run.sh /run.sh
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
