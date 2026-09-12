FROM actualbudget/actual-server:26.9.0-alpine

ARG BUILD_VERSION
ARG BUILD_ARCH

LABEL \
  io.hass.version="$BUILD_VERSION" \
  io.hass.type="app" \
  io.hass.arch="$BUILD_ARCH"

ENV ACTUAL_DATA_DIR=/data
ENV ACTUAL_PORT=5006
ENV ACTUAL_HOSTNAME=0.0.0.0

EXPOSE 5006
