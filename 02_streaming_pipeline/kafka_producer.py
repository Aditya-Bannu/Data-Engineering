# Kafka Producer skeleton

from kafka import KafkaProducer
import json, time, random

# TODO: Configure Kafka producer

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    event = {"user_id": random.randint(1,100), "amount": random.uniform(10,500)}
    producer.send('transactions', event)
    print("Produced:", event)
    time.sleep(2)
