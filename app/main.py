from fastapi import FastAPI

app = FastAPI(title="Sentinel Review")


@app.get("/health")
def health() -> dict[str, str]:
    """Simple endpoint to prove the server is running."""
    return {"status": "ok"}