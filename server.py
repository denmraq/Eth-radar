from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from radar import analyze

app = FastAPI(title="ETH Entry Radar CORE V0.4.0")
BASE = Path(__file__).parent
STATIC = BASE / "static"
app.mount("/static", StaticFiles(directory=STATIC), name="static")

@app.middleware("http")
async def no_stale_ui_cache(request: Request, call_next):
    response = await call_next(request)
    if request.url.path == "/" or request.url.path.startswith("/api/") or request.url.path in {"/service-worker.js", "/manifest.webmanifest"}:
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response

@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")

@app.get("/manifest.webmanifest")
def manifest():
    return FileResponse(STATIC / "manifest.webmanifest", media_type="application/manifest+json")

@app.get("/service-worker.js")
def service_worker():
    return FileResponse(STATIC / "service-worker.js", media_type="application/javascript", headers={"Cache-Control":"no-cache"})

@app.get("/api/health")
def health():
    return {"ok": True, "version": "core-0.4.0"}

@app.get("/api/radar")
def radar():
    return analyze().to_dict()
