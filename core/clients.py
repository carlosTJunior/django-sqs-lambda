import boto3

from django.conf import settings


class AWSSQSClient:
    def __init__(self):
        self.sqs = boto3.client("sqs")
        self.queue = settings.AWS_SQS_QUEUE_URL

    def send_message(self, message: str):
        return self.sqs.send_message(
            QueueUrl=self.queue,
            MessageBody=message
        )
