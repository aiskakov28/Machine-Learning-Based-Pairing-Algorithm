import os, time, requests

BASE = os.getenv("API_URL", "http://localhost:8000")

def wait_ready(path="/healthz", sec=20):
    for _ in range(sec*2):
        try:
            r = requests.get(BASE + path, timeout=2)
            if r.ok:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False

def test_health():
    assert wait_ready()

def test_match_endpoint():
    assert wait_ready()
    payload = {
        "major": "Computer Science",
        "class_year": 2028,
        "academic_interests": "machine learning ai",
        "hobbies": "chess"
    }
    r = requests.post(BASE + "/match?k=5", json=payload, timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list) and len(data) > 0
    assert "score" in data[0]
