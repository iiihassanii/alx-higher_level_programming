#!/bin/bash
# methods the server will accept.
curl -isX OPTIONS $1 | awk '/^Allow:/ {gsub(/^Allow: /, ""); print}'
