import os, json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch

BROKERS = os.getenv("KAFKA_BROKERS", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "profiles")
ES_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
INDEX = os.getenv("ELASTIC_INDEX", "profiles")

es = Elasticsearch(ES_URL)
if not es.indices.exists(index=INDEX):
    es.indices.create(index=INDEX, ignore=400)

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BROKERS.split(","),
    value_deserializer=lambda m: json.loads(m.decode()),
    enable_auto_commit=True,
    group_id=os.getenv("GROUP_ID", "es-indexer"),
)

for msg in consumer:
    body = msg.value
    es.index(index=INDEX, document=body, id=body.get("full_name"))
