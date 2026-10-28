#!/usr/bin/env bash
set -euo pipefail
for url in \
  http://localhost:8001/health \
  http://localhost:8002/health \
  http://localhost:8003/health \
  http://localhost:8001/users/1 \
  http://localhost:8002/products/1 \
  http://localhost:8003/orders/1
do
  echo "Checking $url"
  curl --fail --silent --show-error "$url"
  echo
done
