from src.controllers.candidates import CandidateController
from src.schemas.candidate import (
    CandidateGetResponse,
    CandidateGet,
    CandidateCreateResponse,
    CandidateCreate,
)
from fastapi import APIRouter, Response

router = APIRouter(prefix="/candidates", tags=["candidates"])

controller = CandidateController()


@router.get("/", response_model=CandidateGetResponse)
def get_candidates(response: Response):
    result = controller.get_candidates()
    response.status_code = result.code
    return result


@router.get("/{candidate_id}", response_model=CandidateGetResponse)
def get_candidate_by_id(candidate_id: int, response: Response):
    result = controller.get_candidate_by_id(CandidateGet(id=candidate_id))
    response.status_code = result.code
    return result


@router.post("/", response_model=CandidateCreateResponse)
def create_candidate(data: CandidateCreate, response: Response):
    result = controller.add_user(data)
    response.status_code = result.code
    return result
