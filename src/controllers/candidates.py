from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from src.models.candidate import Candidate
from src.schemas.candidate import (
    CandidateCreate,
    CandidateGet,
    CandidateCreateResponse,
    CandidateGetResponse,
)
from src.services.db import engine


class CandidateController:
    def add_user(self, data: CandidateCreate) -> CandidateCreateResponse:
        try:
            with Session(engine) as session:
                candidate = Candidate(**data.model_dump())

                session.add(candidate)
                session.commit()

            return CandidateCreateResponse(
                msg="Candidate created!",
                code=201,
            )

        except IntegrityError:
            return CandidateCreateResponse(
                msg="Candidate violates a database constraint.",
                code=409,
            )

        except SQLAlchemyError:
            return CandidateCreateResponse(
                msg="Database error occurred.",
                code=500,
            )

    def get_candidate_by_id(self, data: CandidateGet) -> CandidateGetResponse:
        try:
            with Session(engine) as session:
                candidate = session.get(Candidate, data.id)

                if candidate is None:
                    return CandidateGetResponse(
                        data=None,
                        msg="Candidate not found.",
                        code=404,
                    )

                return CandidateGetResponse(
                    data=CandidateGet.model_validate(candidate),
                    msg="Candidate retrieved successfully.",
                    code=200,
                )

        except SQLAlchemyError:
            return CandidateGetResponse(
                data=None,
                msg="Database error occurred.",
                code=500,
            )

    def get_candidates(self) -> CandidateGetResponse:
        try:
            with Session(engine) as session:
                candidates = session.scalars(select(Candidate)).all()

                return CandidateGetResponse(
                    data=[
                        CandidateGet.model_validate(candidate)
                        for candidate in candidates
                    ],
                    msg="Candidates retrieved successfully.",
                    code=200,
                )

        except SQLAlchemyError:
            return CandidateGetResponse(
                data=None,
                msg="Database error occurred.",
                code=500,
            )
