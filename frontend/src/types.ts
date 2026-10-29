export type CatalogEntry = {
  id: string;
  name: string;
  description: string;
  implemented: boolean;
};
export type GameEntry = CatalogEntry & { preview_available: boolean };
export type Catalog = {
  games: GameEntry[];
  algorithms: CatalogEntry[];
  heuristics: CatalogEntry[];
};
export type BoardPreview = {
  game_id: string;
  size: number;
  tiles: number[];
  goal: number[];
  interactive: false;
};
