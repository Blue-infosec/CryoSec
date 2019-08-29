from __future__ import print_function
import boto3
import json
from  emulate_dynamo import emulate_dynamo

# Just a test lambda, run with:
# docker run --rm -v "$PWD":/var/task lambci/lambda:python2.7
# OR
# docker run --rm -v "$PWD":/var/task lambci/lambda:python3.6
# OR
# docker run --rm -v "$PWD":/var/task lambci/lambda:python3.7 lambda_function.lambda_handler

print('Loading function')
#dynamo = boto3.client('dynamodb')
dynamo = emulate_dynamo()

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
        #'GET': lambda dynamo, x: dynamo.query(**x),
        #'POST': lambda dynamo, x: dynamo.put_item(**x),
        #'PUT': lambda dynamo, x: dynamo.update_item(**x),
        #'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
        'DELETE': lambda x: dynamo.del_query(x),
        'GET': lambda x: dynamo.get_query(x),
        'POST': lambda x: dynamo.post_query(x),
        'PUT': lambda x: dynamo.put_query(x)
    }

    operation = event['httpMethod']
    if operation in operations:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])

        #return respond(None, operations[operation](dynamo, payload))
        return respond(None, operations[operation](payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
