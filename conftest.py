import app
import pytest

@pytest.fixture
def api(monkeypatch):
    api = app.app.test_client()
    return api