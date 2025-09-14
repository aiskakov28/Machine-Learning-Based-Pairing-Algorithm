import os
from typing import List, Optional
import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from ..ml.ranker import Ranker

CSV_FALLBACK = os.getenv("CSV_PATH", "data/raw/student_profiles.csv")
CASSANDRA_HOSTS = os.getenv("CASSANDRA_HOSTS", "127.0.0.1").split(",")
KEYSPACE = os.getenv("CASSANDRA_KEYSPACE", "mentor")
TABLE = os.getenv("CASSANDRA_TABLE", "profiles")
MENTEE_YEAR = int(os.getenv("MENTEE_YEAR", "2028"))

app = FastAPI(title="Mentor Match API")

class ProfileIn(BaseModel):
    full_name: Optional[str] = None
    major: str
    class_year: int
    academic_interests: str
    hobbies: str = ""

ranker: Optional[Ranker] = None

def load_df() -> pd.DataFrame:
    try:
        cluster = Cluster(CASSANDRA_HOSTS)
        session = cluster.connect(KEYSPACE)
        stmt = SimpleStatement(f"SELECT full_name, major, class_year, academic_interests, hobbies FROM {TABLE}")
        rows = session.execute(stmt)
        df = pd.DataFrame(list(rows))
        cluster.shutdown()
        if not df.empty:
            return df
    except Exception:
        pass
    return pd.read_csv(CSV_FALLBACK)

@app.on_event("startup")
def bootstrap():
    global ranker
    df = load_df()
    mentors = df[df["class_year"] < MENTEE_YEAR].copy()
    mentors["full_name"] = mentors.get("full_name", pd.Series(range(len(mentors)))).fillna("mentor")
    ranker = Ranker(mentors)

@app.get("/healthz")
def health():
    return {"ok": True}

@app.post("/match")
def match(p: ProfileIn, k: int = Query(10, ge=1, le=50)):
    assert ranker is not None
    results = ranker.rank(p.dict(), top_k=k)
    return results

@app.get("/matches")
def matches(limit: int = Query(10, ge=1, le=50), major: Optional[str] = None):
    assert ranker is not None
    probe = {
        "major": major or "",
        "class_year": MENTEE_YEAR,
        "academic_interests": "",
        "hobbies": "",
        "full_name": None,
    }
    return ranker.rank(probe, top_k=limit)
