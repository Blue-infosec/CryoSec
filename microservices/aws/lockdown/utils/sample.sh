#!/bin/bash

curl -X GET -H "Content-type: application/json" -H "Accept: application/json" -d @utils/event.json https://omdul8jp29.execute-api.us-west-2.amazonaws.com/default/vulndb
