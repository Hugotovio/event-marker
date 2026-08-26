from fastapi import FastAPI

from app.api.v1.invitations import router as invitations_router


app = FastAPI(
    title="Event Maker API",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(
    invitations_router,
    prefix="/api/v1",
)