import { useEffect, useMemo, useState } from "react";
import Layout from "../components/Layout";
import MatchTable from "../components/MatchTable";
import { fetchMatches, Match } from "../lib/api";

export default function Home() {
  const [k, setK] = useState(5);
  const [data, setData] = useState<Match[] | null>(null);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    let mounted = true;
    setLoading(true);
    setErr(null);
    fetchMatches(k)
      .then((d) => mounted && setData(d))
      .catch((e) => mounted && setErr(String(e)))
      .finally(() => mounted && setLoading(false));
    return () => {
      mounted = false;
    };
  }, [k]);

  const menteeCount = useMemo(() => new Set((data || []).map((r) => r.mentee)).size, [data]);

  return (
    <Layout>
      <section style={{ display: "grid", gap: 14, gridTemplateColumns: "1fr auto" }}>
        <div>
          <div style={{ fontSize: 13, opacity: 0.9 }}>Top-K per mentee</div>
          <input
            type="range"
            min={1}
            max={20}
            value={k}
            onChange={(e) => setK(parseInt(e.target.value, 10))}
            style={{ width: 260 }}
          />
          <span style={{ marginLeft: 10, fontWeight: 600 }}>{k}</span>
        </div>
        <div style={{ alignSelf: "end", fontSize: 13, opacity: 0.9 }}>
          Mentees: <b>{menteeCount || 0}</b> • Rows: <b>{data?.length || 0}</b>
        </div>
      </section>

      <div style={{ marginTop: 18 }}>
        {loading && <div>Loading…</div>}
        {err && <div style={{ color: "#ff8a8a" }}>{err}</div>}
        {!loading && !err && <MatchTable rows={data || []} />}
      </div>
    </Layout>
  );
}
