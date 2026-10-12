from fastapi import FastAPI

app = FastAPI(title="AeroOps API")


@app.get("/health")
def health():
    return {"status": "ok"}
