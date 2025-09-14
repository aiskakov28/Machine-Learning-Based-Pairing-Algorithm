import os, json
from kafka import KafkaConsumer
from cassandra.cluster import Cluster

BROKERS = os.getenv("KAFKA_BROKERS", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "profiles")

HOSTS = os.getenv("CASSANDRA_HOSTS", "127.0.0.1").split(",")
KEYSPACE = os.getenv("CASSANDRA_KEYSPACE", "mentor")
TABLE = os.getenv("CASSANDRA_TABLE", "profiles")

cluster = Cluster(HOSTS)
session = cluster.connect()
session.execute(f"CREATE KEYSPACE IF NOT EXISTS {KEYSPACE} WITH replication = {{'class':'SimpleStrategy','replication_factor':1}}")
session.set_keyspace(KEYSPACE)
session.execute(
    f"""CREATE TABLE IF NOT EXISTS {TABLE}(
        full_name text PRIMARY KEY,
        major text,
        class_year int,
        academic_interests text,
        hobbies text
    )"""
)

insert = session.prepare(f"INSERT INTO {TABLE} (full_name, major, class_year, academic_interests, hobbies) VALUES (?,?,?,?,?)")

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BROKERS.split(","),
    value_deserializer=lambda m: json.loads(m.decode()),
    enable_auto_commit=True,
    group_id=os.getenv("GROUP_ID", "cassandra-sink"),
)

for msg in consumer:
    v = msg.value
    session.execute(insert, [
        v.get("full_name"),
        v.get("major"),
        int(v.get("class_year")),
        v.get("academic_interests", ""),
        v.get("hobbies", ""),
    ])
