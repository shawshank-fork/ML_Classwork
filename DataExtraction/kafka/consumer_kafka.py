from kafka import KafkaConsumer
import json

# Create Kafka consumer
consumer = KafkaConsumer(
    "test_topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Consumer started Listening for messages.\n")

for message in consumer:
    print("Received:", message.value)
