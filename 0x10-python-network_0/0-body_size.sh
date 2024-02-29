#!/bin/bash
# cURL body size 
curl -i $1 2>/dev/null| grep Content-Length | awk '{print $2}'
