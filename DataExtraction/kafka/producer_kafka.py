from kafka import KafkaProducer
import json, time, random

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Producer started Sending messages to Kafka.")

while True:
    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 90), 2)
    }

    producer.send("test_topic", data)
    print("Sent:", data)
    
    time.sleep(2)  # Stream every 2 seconds
