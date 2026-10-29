import type { BoardPreview } from "../types";

const baseUrl = (import.meta.env.VITE_API_BASE_URL || "").replace(/\/$/, "");

export async function loadBoardPreview(signal: AbortSignal): Promise<BoardPreview> {
  const response = await fetch(`${baseUrl}/api/v1/games/eight-puzzle/preview`, { signal });
  if (!response.ok) throw new Error(`API request failed (${response.status})`);
  return response.json() as Promise<BoardPreview>;
}
