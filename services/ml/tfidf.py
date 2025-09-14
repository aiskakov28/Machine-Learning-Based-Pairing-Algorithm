from typing import Iterable, Tuple
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def build_text(df: pd.DataFrame) -> pd.Series:
    cols = ["major", "academic_interests", "hobbies"]
    parts = [df[c].fillna("") for c in cols if c in df.columns]
    return (" " + " ".join([""] * len(parts))).join([p.astype(str) for p in parts]).str.strip()

def fit_vectorizer(corpus: Iterable[str]) -> TfidfVectorizer:
    v = TfidfVectorizer(stop_words="english", min_df=1)
    v.fit(corpus)
    return v

def vectorize(v: TfidfVectorizer, texts: Iterable[str]):
    return v.transform(texts)

def fit_transform(df: pd.DataFrame) -> Tuple[TfidfVectorizer, any]:
    text = build_text(df)
    v = fit_vectorizer(text)
    X = v.transform(text)
    return v, X
