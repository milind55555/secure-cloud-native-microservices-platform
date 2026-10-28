import importlib.util
from pathlib import Path
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]

def load_app(service):
    path = ROOT / "services" / service / "app.py"
    spec = importlib.util.spec_from_file_location(service.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.app

def test_user_service():
    client = TestClient(load_app("user-service"))
    assert client.get("/health").status_code == 200
    assert client.get("/users/1").json()["id"] == 1
    assert client.get("/users/999").status_code == 404

def test_product_service():
    client = TestClient(load_app("product-service"))
    assert client.get("/products/1").json()["price"] == 19.99

def test_order_service():
    client = TestClient(load_app("order-service"))
    assert client.get("/orders/1").json()["status"] == "created"
