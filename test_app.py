from app import app

def test_healthz():
    response = app.test_client().get("/healthz")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_index_has_version():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "version" in response.get_json()

def test_metrics_exposed():
    response = app.test_client().get("/metrics")
    assert response.status_code == 200
    assert response.data != b""
