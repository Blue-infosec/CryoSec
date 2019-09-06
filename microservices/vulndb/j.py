#!/usr/bin/env python3.7

import json
var='''
{
  "httpMethod": "POST",
  "queryStringParameters": {
    "TableName": "checklist_redhat",
    "Item": {
      "stig_id": {
        "S": "RHEL-07-010020"
      },
      "status": {
        "S": "Open"
      }
    }
  }
}
'''
print(json.loads(var)["queryStringParameters"])

