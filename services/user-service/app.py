from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI(title="user-service", version="1.0.0")
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["service"])
DATA = {item["id"]: item for item in [{'id': 1, 'name': 'Demo User', 'email': 'user@example.test'}, {'id': 2, 'name': 'Alex Example', 'email': 'alex@example.test'}]}

@app.middleware("http")
async def count_requests(request, call_next):
    response = await call_next(request)
    REQUESTS.labels(service="user-service").inc()
    return response

@app.get("/health")
def health():
    return {"status": "ok", "service": "user-service"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/users")
def list_users():
    return list(DATA.values())

@app.get("/users/{item_id}")
def get_user(item_id: int):
    item = DATA.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="user not found")
    return item
