import pandas as pd
from services.ml.tfidf import fit_transform, build_text

def test_fit_transform_shapes():
    df = pd.DataFrame([
        {"major":"CS","academic_interests":"ai ml","hobbies":"chess"},
        {"major":"Math","academic_interests":"algebra","hobbies":"piano"},
    ])
    v, X = fit_transform(df)
    assert X.shape[0] == 2
    assert len(v.get_feature_names_out()) > 0

def test_build_text_nonempty():
    df = pd.DataFrame([{"major":"CS","academic_interests":"ai","hobbies":"run"}])
    txt = build_text(df).iloc[0]
    assert isinstance(txt, str) and len(txt) > 0
