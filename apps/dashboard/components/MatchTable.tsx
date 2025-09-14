import { Match } from "../lib/api";

export default function MatchTable({ rows }: { rows: Match[] }) {
  return (
    <div style={{ overflowX: "auto", border: "1px solid #1f2740", borderRadius: 10 }}>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead style={{ background: "#121735" }}>
          <tr>
            <th style={th}>Mentee</th>
            <th style={th}>Mentor</th>
            <th style={th}>Mentor Major</th>
            <th style={thRight}>Score</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r, i) => (
            <tr key={`${r.mentee}-${r.mentor}-${i}`} style={{ borderTop: "1px solid #1f2740" }}>
              <td style={td}>{r.mentee}</td>
              <td style={td}>{r.mentor}</td>
              <td style={td}>{r.mentor_major}</td>
              <td style={tdRight}>{r.score.toFixed(3)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const th = { textAlign: "left" as const, padding: "12px 14px", fontWeight: 600, fontSize: 13 };
const thRight = { ...th, textAlign: "right" as const };
const td = { padding: "12px 14px", fontSize: 14 };
const tdRight = { ...td, textAlign: "right" as const };
