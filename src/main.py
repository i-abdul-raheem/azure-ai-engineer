from fastapi import FastAPI, Response

from src.routes.candidates import router as candidate_router

app = FastAPI(title="Candidate Management API", version="0.1")

app.include_router(candidate_router)


@app.get("/health")
def health(response: Response):
    return Response({"msg": "I am up"}, 200)
