from fastapi.testclient import TestClient
from app.main import create_app

client = TestClient(create_app())


def test_health():
    assert client.get("/api/v1/health").json()["status"] == "ok"


def test_catalog_does_not_claim_planned_features_are_implemented():
    response = client.get("/api/v1/catalog")
    assert response.status_code == 200
    catalog = response.json()
    for entries in catalog.values():
        assert entries
        assert len({entry["id"] for entry in entries}) == len(entries)
        assert all(entry["implemented"] is False for entry in entries)
    assert catalog["games"][0]["preview_available"] is True


def test_preview_is_a_valid_static_board():
    response = client.get("/api/v1/games/eight-puzzle/preview")
    assert response.status_code == 200
    board = response.json()
    assert board["interactive"] is False
    assert board["size"] == 3
    assert sorted(board["tiles"]) == sorted(board["goal"]) == list(range(9))


def test_unavailable_game_returns_404():
    assert client.get("/api/v1/games/maze/preview").status_code == 404


def test_no_solver_or_game_mutation_is_exposed():
    assert client.post("/api/v1/solve", json={}).status_code == 404
    assert client.post("/api/v1/games/eight-puzzle/preview", json={}).status_code == 405


def test_cors_allows_only_configured_origins():
    allowed = client.get("/api/v1/health", headers={"Origin": "http://localhost:5174"})
    assert allowed.headers["access-control-allow-origin"] == "http://localhost:5174"
    denied = client.get("/api/v1/health", headers={"Origin": "https://unconfigured.example"})
    assert "access-control-allow-origin" not in denied.headers
