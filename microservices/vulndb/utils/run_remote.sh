#!/bin/bash
#json=$(cat sam-app/events/event.json)
json=$(cat event.json.new)
curl -X GET -d @event.json.new -H "Content-Type: application/json" https://omdul8jp29.execute-api.us-west-2.amazonaws.com/default/vulndb

#curl -X GET -d @event.json.new \
#  -H "Content-Type: application/json" \
#  https://omdul8jp29.execute-api.us-west-2.amazonaws.com/default/vulndb
