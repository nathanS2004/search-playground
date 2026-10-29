# Architecture and extension guide

## Current flow

React → typed HTTP client → `/api/v1` routes → catalog and board response models.

The frontend loads only the static 8-puzzle preview. If Python is unavailable, it keeps an identical local board. The page consists of one heading, the board, and one explanatory paragraph. There are no menus, configuration panels, result sections, or game interactions. The catalog endpoint remains available for future development.

## Boundaries

- `PuzzleBoard` renders numbers and an empty slot. It has no click handlers, move rules, or mutable game state.
- `catalog.py` lists planned capabilities. Listing an algorithm does not mean it exists.
- `domain/contracts.py` is independent of HTTP and UI. Hashable states allow future search implementations to track visited states.
- `SearchProblem` supplies initial state, goal detection, and weighted transitions. `Solver` accepts a problem, heuristic, and limits, returning path, actions, and metrics. These are interfaces only.
- The FastAPI app factory supports isolated tests. CORS permits explicitly configured frontend origins.

## Adding a game

Create a module under `backend/app/domain/` for the game's rules and state representation. Test legal moves, impossible moves, state validity, and goal detection there. Implement `SearchProblem` for single-agent search. Update the catalog's availability flag only after the implementation exists and is actually wired into an endpoint and frontend.

For the 8-puzzle, exclude the empty slot from tile-distance heuristics. Scramble by legal moves to ensure solvability; scramble move count is not necessarily optimal solution depth.

## Adding a solver

Keep search functions separate from game rules and routes. Implement one algorithm, add tests with known optimal paths, expose validated request/response models, and connect the client. Define result status values for success, no solution, cancellation, and resource limits when those behaviors are implemented. Never report a limit or cancellation as a solved puzzle.

Run CPU-heavy searches in a bounded worker/process or job service. The placeholder `SearchLimits` does not enforce anything by itself. Enforce limits and cancellation in the solver runner before accepting expensive public searches. Define metrics consistently across algorithms and keep animation time separate from search time.

## Production configuration

The frontend is a static bundle; the backend remains a separate Python service. Configure a public API origin at build time, or route `/api` to Python through a reverse proxy. Use HTTPS for both. Scope backend CORS to the deployed frontend. No persistence, authentication, job execution, or deployment infrastructure is included yet.
