from enum import Enum

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StatusEnum(str, Enum):
    applied = "applied"
    interview = "interview"
    hired = "hired"
    rejected = "rejected"


class CandidateCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    skills: list[str]
    experience: int = Field(ge=0)
    status: StatusEnum = StatusEnum.applied


class CandidateGet(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CandidateUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    skills: list[str] | None = None
    experience: int | None = Field(default=None, ge=0)
    status: StatusEnum | None = None


class CandidateCreateResponse(BaseModel):
    msg: str
    code: int


class CandidateGetResponse(BaseModel):
    data: CandidateGet | list[CandidateGet] | None = None
    msg: str | None = None
    code: int


class CandidateUpdateResponse(CandidateCreateResponse):
    pass


class CandidateDeleteResponse(CandidateCreateResponse):
    pass


class CandidateDelete(BaseModel):
    id: int