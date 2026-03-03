import pika
import json
import time
from tasks import process_task


def connect_to_rabbit():
    while True:
        try:
            credentials = pika.PlainCredentials("guest", "guest")
            parameters = pika.ConnectionParameters(
                host="rabbitmq",
                credentials=credentials
            )

            connection = pika.BlockingConnection(parameters)
            print("✅ Conectado a RabbitMQ")
            return connection

        except pika.exceptions.AMQPConnectionError:
            print("⏳ RabbitMQ no está listo, reintentando en 5 segundos...")
            time.sleep(5)


def callback(ch, method, properties, body):

    print("Mensaje recibido:",body)
    data = json.loads(body)
    process_task(data)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 👇 USAMOS la conexión con retry
connection = connect_to_rabbit()
channel = connection.channel()

channel.queue_declare(queue="peliculas")

channel.basic_consume(
    queue="peliculas",
    on_message_callback=callback
)

print("🎧 Worker esperando mensajes...")
channel.start_consuming()