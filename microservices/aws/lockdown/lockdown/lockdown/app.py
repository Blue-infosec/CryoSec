import boto3
import json
from receive_message import retrieve_sqs_messages
from send_message import send_sqs_message

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
        'GET': lambda dynamo, x: dynamo.scan(**x),
        'POST': lambda dynamo, x: dynamo.put_item(**x),
        'PUT': lambda dynamo, x: dynamo.update_item(**x),
    }

    operation = event['httpMethod']
    if operation in operations:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
        sqs_queue_url="https://sqs.us-west-2.amazonaws.com/096412041307/lockdown_q.fifo"
        #retrieve_sqs_messages(sqs_queue_url, num_msgs=1, wait_time=2, visibility_time=5)
        #delete_sqs_message(sqs_queue_url, msg_receipt_handle)
        msg_body='SQS message'
        group_id="lambda_lockdown_req"
        dedup_id="lambda_lockdown_req"
        #return respond(None, operations[operation](dynamo, payload))
        return respond(None, send_sqs_message(sqs_queue_url, msg_body, group_id, dedup_id))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
# New data
