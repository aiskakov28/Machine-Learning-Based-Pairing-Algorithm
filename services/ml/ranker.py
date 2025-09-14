from typing import List, Dict
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .tfidf import build_text, fit_vectorizer, vectorize

class Ranker:
    def __init__(self, mentors: pd.DataFrame):
        self.mentors = mentors.reset_index(drop=True)
        self.mentors_text = build_text(self.mentors)
        self.v = fit_vectorizer(self.mentors_text)
        self.X = self.v.transform(self.mentors_text)

    def rank(self, profile: Dict, top_k: int = 10) -> List[Dict]:
        probe = pd.DataFrame([{
            "major": profile.get("major", ""),
            "academic_interests": profile.get("academic_interests", ""),
            "hobbies": profile.get("hobbies", "")
        }])
        y = vectorize(self.v, build_text(probe))
        s = cosine_similarity(y, self.X).ravel()
        idx = np.argsort(-s)[:top_k]
        out = []
        for i in idx:
            row = self.mentors.iloc[i]
            out.append({
                "full_name": row.get("full_name", f"mentor-{i}"),
                "major": row.get("major", ""),
                "class_year": int(row.get("class_year", 0)),
                "academic_interests": row.get("academic_interests", ""),
                "hobbies": row.get("hobbies", ""),
                "score": float(s[i]),
            })
        return out
