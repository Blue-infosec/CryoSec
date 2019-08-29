from __future__ import print_function
import boto3
import json

# Just a test lambda, run with:
# docker run --rm -v "$PWD":/var/task lambci/lambda:python2.7
# OR
# docker run --rm -v "$PWD":/var/task lambci/lambda:python3.6
# OR
# docker run --rm -v "$PWD":/var/task lambci/lambda:python3.7 lambda_function.lambda_handler
def json_resp(payload):
    sample_data = {"Items":
      [
        {"stig_id": {"S": "RHEL-07-010020"}, "status": {"S": "Not_A_Finding"}},
        {"stig_id": {"S": "RHEL-07-010010"}, "status": {"S": "Open"}}
      ]
    }
    return [item for item in payload if item in payload["queryStringParameters"]]

payload = {
  "httpMethod": "GET",
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

print('Loading function')
dynamo = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

    operations = {
        'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
        #'GET': lambda dynamo, x: dynamo.query(**x),
        #'POST': lambda dynamo, x: dynamo.put_item(**x),
        'GET': lambda x: json_resp(**x),
        'POST': lambda dynamo, x: dynamo.put_item(**x),
        'PUT': lambda dynamo, x: dynamo.update_item(**x),
    }

    operation = event['httpMethod']
    if operation in operations:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
        #return respond(None, operations[operation](dynamo, payload))
        return respond(None, operations[operation](payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))



#from __future__ import print_function
#import os
#import sys
#import subprocess

#def lambda_handler(event, context):
#    context.log('Hello!')
#    context.log('Hmmm, does not add newlines in 3.7?')
#    context.log('\n')
#
#    print(sys.executable)
#    print(sys.argv)
#    print(os.getcwd())
#    print(__file__)
#    print(os.environ)
#    print(context.__dict__)
#
#    return {
#        "executable": str(sys.executable),
#        "sys.argv": str(sys.argv),
#        "os.getcwd": str(os.getcwd()),
#        "__file__": str(__file__),
#        "os.environ": str(os.environ),
#        "context.__dict__": str(context.__dict__),
#        "ps aux": str(subprocess.check_output(['ps', 'aux'])),
#        "event": event
#    }

