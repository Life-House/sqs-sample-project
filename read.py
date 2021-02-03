import boto3

from config import SQS_READ_QUEUE, AWS_REGION

# Create SQS client
sqs_client = boto3.client('sqs', region_name=AWS_REGION)

# Receive message from SQS queue
response = sqs_client.receive_message(
    QueueUrl=SQS_READ_QUEUE,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']
print(len(response['Messages']))
# Delete received message from queue once consumed
# sqs_client.delete_message(
#     QueueUrl=SQS_READ_QUEUE,
#     ReceiptHandle=receipt_handle
# )
print('Received and deleted message: %s' % message)
