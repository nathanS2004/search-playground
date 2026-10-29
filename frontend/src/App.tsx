import { useEffect, useState } from "react";
import { PuzzleBoard } from "./components/PuzzleBoard";
import { loadBoardPreview } from "./lib/api";

const initialTiles = [1, 2, 3, 4, 0, 6, 7, 5, 8];

export default function App() {
  const [tiles, setTiles] = useState(initialTiles);

  useEffect(() => {
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 8000);
    loadBoardPreview(controller.signal)
      .then((preview) => {
        if (!controller.signal.aborted) setTiles(preview.tiles);
      })
      .catch(() => {
        // The same static preview remains usable when developing without Python.
      })
      .finally(() => window.clearTimeout(timeout));
    return () => {
      controller.abort();
      window.clearTimeout(timeout);
    };
  }, []);

  return (
    <main className="puzzle-page">
      <h1>8-puzzle</h1>
      <PuzzleBoard tiles={tiles} />
      <p>
        A small project for comparing how search algorithms solve the 8-puzzle
        using different distance heuristics. This is a static starting board;
        tile movement and solvers will be added later.
      </p>
    </main>
  );
}
