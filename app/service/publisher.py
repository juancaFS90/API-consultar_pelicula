import pika
import json

def publish_message(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )
    channel = connection.channel()

    channel.queue_declare(queue="peliculas")

    channel.basic_publish(
        exchange="",
        routing_key="peliculas",
        body=json.dumps(message)
    )

    connection.close()