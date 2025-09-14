import { fetchMatches } from "../lib/api";

describe("fetchMatches", () => {
  const g: any = global;
  beforeEach(() => {
    g.fetch = jest.fn(() =>
      Promise.resolve({ ok: true, json: () => Promise.resolve([]) })
    );
  });

  it("calls API with k", async () => {
    await fetchMatches(3);
    expect(g.fetch).toHaveBeenCalledWith(
      "http://localhost:8000/matches?k=3",
      expect.any(Object)
    );
  });
});
