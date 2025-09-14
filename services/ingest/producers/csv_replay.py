import os, time, json, csv
from kafka import KafkaProducer

CSV_PATH = os.getenv("CSV_PATH", "data/raw/student_profiles.csv")
BROKERS = os.getenv("KAFKA_BROKERS", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "profiles")

producer = KafkaProducer(bootstrap_servers=BROKERS.split(","), value_serializer=lambda v: json.dumps(v).encode())

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        msg = {
            "full_name": row.get("Full_name") or row.get("full_name"),
            "major": row.get("major"),
            "class_year": int(row.get("class_year")),
            "academic_interests": row.get("academic_interests", ""),
            "hobbies": row.get("hobbies", ""),
            "source": "csv",
        }
        producer.send(TOPIC, msg)
        time.sleep(float(os.getenv("SPEED_DELAY_SEC", "0.05")))
producer.flush()
