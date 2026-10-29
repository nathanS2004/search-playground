type Props = { tiles: number[] };

/** Display only; game rules and movement can be added separately. */
export function PuzzleBoard({ tiles }: Props) {
  return (
    <div
      className="puzzle-board"
      role="img"
      aria-label={`Static 8-puzzle board: ${tiles.map((tile) => tile || "empty").join(", ")}. Tiles are not interactive.`}
    >
      {tiles.map((tile, index) => (
        <div key={index} aria-hidden="true" className={`tile${tile === 0 ? " empty" : ""}`}>
          {tile || null}
        </div>
      ))}
    </div>
  );
}
