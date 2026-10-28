from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI(title="product-service", version="1.0.0")
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["service"])
DATA = {item["id"]: item for item in [{'id': 1, 'name': 'Starter Kit', 'price': 19.99}, {'id': 2, 'name': 'Cloud Notebook', 'price': 8.5}]}

@app.middleware("http")
async def count_requests(request, call_next):
    response = await call_next(request)
    REQUESTS.labels(service="product-service").inc()
    return response

@app.get("/health")
def health():
    return {"status": "ok", "service": "product-service"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/products")
def list_products():
    return list(DATA.values())

@app.get("/products/{item_id}")
def get_product(item_id: int):
    item = DATA.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="product not found")
    return item
