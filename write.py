import boto3
import json
from datetime import datetime
from config import SQS_WRITE_QUEUE, AWS_REGION


sqs_client = boto3.client('sqs', region_name=AWS_REGION)

RAMDOM_ID = str(datetime.now().timestamp())

payload = {
    "customer": "CUSTOMER_ID",
    "hotel": "HOTEL_ID",
    "body": "this is a test message"
}

response = sqs_client.send_message(
    QueueUrl=SQS_WRITE_QUEUE,
    MessageDeduplicationId=RAMDOM_ID,
    MessageGroupId='TEST_GROUP_ID',
    MessageAttributes={},
    MessageBody=(json.dumps(payload))
)

print(response)
