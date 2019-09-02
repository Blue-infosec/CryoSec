#!/bin/bash
#json=$(cat sam-app/events/event.json)
json=$(cat event.json)
curl -X GET -d "$json" \
  https://s7xqtnxxu0.execute-api.us-west-2.amazonaws.com/Prod/hello
