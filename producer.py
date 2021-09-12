import json
import pika

params = pika.URLParameters('amqps://rinseenq:iZkfHfgARAZ5YlARbX6yKDS0yYhxcn-X@beaver.rmq.cloudamqp.com/rinseenq')

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
