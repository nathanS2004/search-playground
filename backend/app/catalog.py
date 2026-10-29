"""Descriptive registry. Entries advertise planned capabilities, not implementations."""
from .schemas import BoardPreview, Catalog, CatalogEntry, GameEntry

CATALOG = Catalog(
    games=[
        GameEntry(id="eight-puzzle", name="8-puzzle", description="Eight tiles. One empty space. A world of possible paths.", preview_available=True),
        GameEntry(id="maze", name="Maze explorer", description="Find a path through a world of obstacles."),
        GameEntry(id="connect-four", name="Connect Four", description="Plan your next move against an opponent."),
    ],
    algorithms=[
        CatalogEntry(id="astar", name="A* search", description="Balances the cost so far with an estimate of the remaining path."),
        CatalogEntry(id="bfs", name="Breadth-first search", description="Explores positions one depth level at a time."),
        CatalogEntry(id="greedy", name="Greedy best-first", description="Explores the position that looks closest to the goal."),
    ],
    heuristics=[
        CatalogEntry(id="manhattan", name="Manhattan distance", description="Adds each numbered tile's horizontal and vertical distance to its goal."),
        CatalogEntry(id="euclidean", name="Euclidean distance", description="Adds each numbered tile's straight-line distance to its goal."),
        CatalogEntry(id="misplaced", name="Misplaced tiles", description="Counts numbered tiles outside their goal positions."),
    ],
)
PREVIEW = BoardPreview(game_id="eight-puzzle", size=3,
    tiles=[1, 2, 3, 4, 0, 6, 7, 5, 8], goal=[1, 2, 3, 4, 5, 6, 7, 8, 0])
