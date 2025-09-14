import { ReactNode } from "react";

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div style={{ minHeight: "100vh", background: "#0b1020", color: "#e6e8ef" }}>
      <header style={{ padding: "16px 20px", borderBottom: "1px solid #1f2740" }}>
        <h1 style={{ margin: 0, fontSize: 22 }}>Mentor Match Dashboard</h1>
      </header>
      <main style={{ padding: 20, maxWidth: 1100, margin: "0 auto" }}>{children}</main>
    </div>
  );
}
