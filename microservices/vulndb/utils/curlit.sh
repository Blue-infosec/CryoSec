event=$(cat event.get.json)
curl -X GET -H 'Content-Type: application/json' \
  "https://omdul8jp29.execute-api.us-west-2.amazonaws.com/default/vulndb"
