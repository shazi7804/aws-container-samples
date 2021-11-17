import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='EcsScalingBySqsStack-queue276F7297-DQMDJ9OYL896')

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5)

    for message in messages:
        print("Activating MessageId: {0}".format(message.message_id))
        print("Message received: {0}".format(message.body))
        message.delete()
        print("Finished for MessageId: {0}".format(message.message_id))