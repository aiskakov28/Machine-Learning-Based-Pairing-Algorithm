import os, requests

class Client:
    def __init__(self, base_url: str | None = None, timeout: int = 10):
        self.base = base_url or os.getenv("MATCH_API", "http://localhost:8080")
        self.timeout = timeout

    def ping(self) -> bool:
        try:
            r = requests.get(f"{self.base}/healthz", timeout=self.timeout)
            return r.ok
        except requests.RequestException:
            return False

    def match(self, profile: dict) -> dict:
        r = requests.post(f"{self.base}/match", json=profile, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def top(self, limit: int = 10) -> list[dict]:
        r = requests.get(f"{self.base}/matches", params={"limit": limit}, timeout=self.timeout)
        r.raise_for_status()
        return r.json()
