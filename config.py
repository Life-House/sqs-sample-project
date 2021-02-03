import os
from dotenv import load_dotenv

load_dotenv()

SQS_READ_QUEUE=os.environ['SQS_READ_QUEUE']
SQS_WRITE_QUEUE=os.environ['SQS_WRITE_QUEUE']
AWS_REGION=os.environ['AWS_REGION']