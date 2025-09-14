const BASE = process.env.MATCH_API || "http://localhost:8080";

export async function ping() {
  const r = await fetch(`${BASE}/healthz`);
  return r.ok;
}

export async function match(profile) {
  const r = await fetch(`${BASE}/match`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(profile),
  });
  if (!r.ok) throw new Error("match failed");
  return r.json();
}

export async function top(limit = 10) {
  const r = await fetch(`${BASE}/matches?limit=${limit}`);
  if (!r.ok) throw new Error("list failed");
  return r.json();
}

export default { ping, match, top };
