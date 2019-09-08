#!/bin/bash
curl -i -X POST -d @setup/sam-app_files/POST_event.json \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  https://7wioz3xge6.execute-api.us-west-2.amazonaws.com/Prod/hello
echo ""
