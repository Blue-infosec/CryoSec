#!/usr/bin/env python3.7
import json
data = '''{
  "httpMethod": "POST",
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
}'''
#payload = json.loads(data)
payload = data
