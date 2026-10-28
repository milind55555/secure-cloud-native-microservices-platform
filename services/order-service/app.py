from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI(title="order-service", version="1.0.0")
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["service"])
DATA = {item["id"]: item for item in [{'id': 1, 'user_id': 1, 'product_id': 1, 'quantity': 2, 'status': 'created'}, {'id': 2, 'user_id': 2, 'product_id': 2, 'quantity': 1, 'status': 'shipped'}]}

@app.middleware("http")
async def count_requests(request, call_next):
    response = await call_next(request)
    REQUESTS.labels(service="order-service").inc()
    return response

@app.get("/health")
def health():
    return {"status": "ok", "service": "order-service"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/orders")
def list_orders():
    return list(DATA.values())

@app.get("/orders/{item_id}")
def get_order(item_id: int):
    item = DATA.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="order not found")
    return item
