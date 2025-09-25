#!/bin/sh
set -e

ENV_FILE=/usr/share/nginx/html/assets/env-config.js

cat <<EOF > $ENV_FILE
(function (window) {
  window.__env = window.__env || {};
  window.__env.apiUrl = "http://${SERVERIP}:${BACKEND_PORT}";
})(this);
EOF

exec "$@"