const BASE = process.env.NEXT_PUBLIC_MATCH_API || "http://localhost:8000";

export type Match = {
  mentee: string;
  mentor: string;
  score: number;
  mentor_major: string;
};

export async function fetchMatches(k = 5): Promise<Match[]> {
  const res = await fetch(`${BASE}/matches?k=${k}`, { cache: "no-store" });
  if (!res.ok) throw new Error("fetch failed");
  return res.json();
}
