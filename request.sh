#!/bin/bash
  # "httpMethod": "GET",
query='''
{
  "queryStringParameters": {
    "KeyConditionExpression": "stig_id = :item1",
    "ExpressionAttributeValues": {
      ":item1": {
        "S": "RHEL-07-010020"
      }
    },
    "ConsistentRead": true,
    "ReturnConsumedCapacity": "TOTAL",
    "TableName": "checklist_redhat"
  }
}
'''

curl -v -X GET \
  'https://v6bdx6q1cg.execute-api.us-west-2.amazonaws.com/Prod/MyResource' \
  -H 'content-type: application/json' \
  -H "x-api-key:qjekz87AlqatzlICMiRos24Tj20vwOTa9zCP57GH" \
  -d "$query"

# echo "$query"
#  -H 'day: Thursday' \

