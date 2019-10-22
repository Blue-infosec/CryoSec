#!/bin/bash
#echo """{
#    "Messages": [
#        {
#            "Body": "{\"TableName\": \"lockdown\", \"Item\": {\"p_id\": {\"S\": \"6\"}, \"stig_id\": {\"S\": \"RHEL-07-020110\"}, \"action\": {\"S\": \"check\"}, \"action_status\": {\"S\": \"Processing\"}}}",
#            "Attributes": {
#                "ApproximateFirstReceiveTimestamp": "1571432802256",
#                "SequenceNumber": "37295774943002081024",
#                "SenderId": "AROARM4U3ABNRF6JURTVP:lockdown-LockDownFunction-DA27GYNSFA8Y",
#                "MessageDeduplicationId": "lambda_lockdown_req",
#                "SentTimestamp": "1571432795246",
#                "ApproximateReceiveCount": "2",
#                "MessageGroupId": "lambda_lockdown_req"
#            },
#            "ReceiptHandle": "AQEBkEUaIxKiT+9qo7ROSReP6oZXk5i12o5EoK1uRW/3wzunMlTgJ9KMR816r6pbe+6jI5m8Efkb2I/OLZP1ujgTqwmY/wOGblP0fHRL/Q0CJ5nimJ7FwjczTviU569uwPQBftqZxadLlNnMyg/w164AVo8PgUzwuCeDf9LJq9WrRtcRhs4VdmcWUV0o/BnGk7syB7bYtISQa3ntFVrwF5DVfNYmP4eUtsIYYV1CjGgu0y7a+j+f0X3WkaDR5eRkEoxprqS3urBq4KESXZMUn7Ybtw==",
#            "MD5OfBody": "c65c6875d303369cbbc1ab565d4b2267",
#            "MessageId": "ea15f83d-0fa2-4e97-ac4b-1a57cfb6fe03"
#        }
#    ]
#}""" | awk /"ReceiptHandle"/ | tr -d " \t\n\r" | sed 's/,//g' | sed 's/ReceiptHandle://g'
#response=$(aws sqs receive-message --queue-url https://sqs.us-west-2.amazonaws.com/096412041307/lockdown_q.fifo --attribute-names All --message-attribute-names All --max-number-of-messages 1 | awk /"Body"/ | tr -d " \t\n\r" | sed 's/,//g' | sed 's/\"Body\"://g')
response=$(aws sqs receive-message --queue-url https://sqs.us-west-2.amazonaws.com/096412041307/lockdown_deadq.fifo --attribute-names All --message-attribute-names All --max-number-of-messages 1 | awk /"Body"/ | tr -d " \t\n\r" | sed 's/,//g' | sed 's/\"Body\":\"//g' | sed 's/""MD5OfBody".*//' | sed 's/\\//g')
echo "$response"
#message=$(echo $response | awk /"Body"/ | tr -d " \t\n\r" | sed 's/,//g' | sed 's/Body://g')
#message=$(echo "$response" )

#reciept_handle=$(echo $response | awk /"ReceiptHandle"/ | tr -d " \t\n\r" | sed 's/,//g' | sed 's/ReceiptHandle://g')

#aws sqs delete-message --queue-url https://sqs.us-west-2.amazonaws.com/096412041307/lockdown_q.fifo --receipt-handle $reciept_handle

echo "$message"
echo "$reciept_handle"
