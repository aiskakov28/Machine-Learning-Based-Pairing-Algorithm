import pandas as pd
from services.ml.ranker import Ranker

def test_rank_returns_sorted():
    mentors = pd.DataFrame([
        {"full_name":"A","major":"Computer Science","class_year":2026,"academic_interests":"ai ml","hobbies":"chess"},
        {"full_name":"B","major":"Biology","class_year":2025,"academic_interests":"genetics","hobbies":"hike"},
    ])
    r = Ranker(mentors)
    probe = {"major":"Computer Science","class_year":2028,"academic_interests":"machine learning","hobbies":""}
    res = r.rank(probe, top_k=2)
    assert len(res) == 2
    assert res[0]["full_name"] == "A"
    assert res[0]["score"] >= res[1]["score"]
