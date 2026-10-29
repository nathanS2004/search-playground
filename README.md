# Search Playground

A visual lab for exploring how search algorithms approach the same problem.

**Status: foundation / v0.1.** This repository intentionally contains no playable games or solver implementations. The 8-puzzle tiles are static. The page contains just the board, a heading, and one short paragraph about the project.

## What's included

- Minimal, responsive React + TypeScript + Vite page.
- A static 3×3 puzzle board with tiles 1–8 and one empty space.
- FastAPI backend serving a real catalog, health check, and static board data.
- Typed API client that loads the board from Python, with the same local static board as a fallback.
- Game-independent Python protocols for future search problems, solvers, results, and limits.
- API tests and GitHub Actions checks for Python and the frontend production build.

## Run locally

Requires Node.js 22.12+ (Node 24 recommended) and Python 3.11+.

### 1. Python API

From the repository root:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[dev]"
.venv\Scripts\python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

On macOS/Linux, substitute `.venv/bin/python` for `.venv\Scripts\python`.

API documentation: http://127.0.0.1:8001/docs

### 2. Frontend

In a second terminal, from the repository root:

```sh
cd frontend
npm ci
npm run dev
```

Open http://127.0.0.1:5174. The Vite development server proxies `/api` to Python on port 8001. These ports avoid the common 5173/8000 defaults. Start both servers to load the board from Python. The same static board remains visible if the API is offline; the paragraph explains that this version is a static preview.

### Checks

```sh
# From frontend/
npm run build

# From backend/, after installing .[dev]
python -m pytest
```

Use the virtual environment's Python if it is not activated.

## Project layout

```text
frontend/
  src/
    components/PuzzleBoard.tsx  # Display-only tiles
    lib/api.ts                 # All HTTP requests
    types.ts                   # API response types
    App.tsx                    # Single puzzle page
    styles.css                 # Responsive design
backend/
  app/
    domain/contracts.py        # Future problem/solver interfaces
    catalog.py                 # Metadata and static preview
    schemas.py                 # API response models
    routes.py                  # Versioned HTTP endpoints
    main.py                    # App factory and CORS
  tests/test_api.py
.github/workflows/checks.yml
```

## API

| Method | Path                                 | Purpose                                   |
| ------ | ------------------------------------ | ----------------------------------------- |
| GET    | `/api/v1/health`                     | Service health                            |
| GET    | `/api/v1/catalog`                    | Planned games, algorithms, and heuristics |
| GET    | `/api/v1/games/eight-puzzle/preview` | Static starting board and goal            |

Every catalog item reports `implemented: false`. Only the 8-puzzle has `preview_available: true`. There is deliberately no move or solve endpoint yet.

## Where to start building

1. Add an 8-puzzle domain module containing legal moves, goal detection, and solvable shuffling.
2. Add board state and movement handlers around `PuzzleBoard`; keep rules out of display components.
3. Implement `SearchProblem` and A* with Manhattan distance through the `Solver` protocol.
4. Add validated solve request/response models and execution limits, then add a small solver control to the page. CPU-heavy search should run outside the API event loop, with cancellation and time/expansion bounds.
5. Add real metrics, animation, and comparisons on identical starting states.
6. Add maze navigation. Connect Four needs a separate adversarial-game interface; don't force it into single-agent pathfinding.

See [architecture notes](docs/architecture.md) for the data flow and extension boundaries.

## Hosting later

The repository being public does not deploy the application. Build the frontend with `npm run build` and publish `frontend/dist` to a static host. Run FastAPI on a Python-capable host. Set `VITE_API_BASE_URL` to the public API origin **before building** the frontend, and set `FRONTEND_ORIGINS` on the backend to your frontend's exact origin. A same-origin reverse proxy for `/api` is another option. Vite's development proxy is not part of the production build.

The `.env.example` files document configuration. Frontend Vite variables are public. The backend reads OS environment variables; its example file is not auto-loaded. No database, credentials, or paid AI services are needed for this scaffold.

## Stack references

[Vite documentation](https://vite.dev/guide/) · [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/first-steps/)
