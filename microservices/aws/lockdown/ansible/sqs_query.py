#!/usr/bin/env python3.7
import json
import boto3
from receive_message import retrieve_sqs_messages,delete_sqs_message
from send_message import send_sqs_message

#response=$(aws sqs receive-message \
#  --queue-url https://sqs.us-west-2.amazonaws.com/096412041307/lockdown_deadq.fifo \
#  --attribute-names All \
#  --message-attribute-names All \
#  --max-number-of-messages 1)

sqs_queue_url="https://sqs.us-west-2.amazonaws.com/096412041307/lockdown_deadq.fifo"

#Retrieve SQS Message
msg=retrieve_sqs_messages(sqs_queue_url, num_msgs=1, wait_time=2, visibility_time=5)
msg_receipt_handle=msg[0]['ReceiptHandle']

print(msg)
print(msg_receipt_handle)

# Delete SQS message
#delete_sqs_message(sqs_queue_url, msg_receipt_handle)
