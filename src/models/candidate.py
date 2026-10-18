from enum import Enum as PyEnum

from sqlalchemy import String, Enum as SQLEnum, CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class StatusEnum(str, PyEnum):
    applied = "applied"
    interview = "interview"
    hired = "hired"
    rejected = "rejected"


class Candidate(Base):
    __tablename__ = "candidates"

    __table_args__ = (
        CheckConstraint(
            "experience >= 0",
            name="check_experience_nonnegative",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True
    )

    skills: Mapped[list[str]] = mapped_column(
        MutableList.as_mutable(ARRAY(String)),
        nullable=False,
        default=list,
    )

    experience: Mapped[int] = mapped_column(nullable=False)

    status: Mapped[StatusEnum] = mapped_column(
        SQLEnum(StatusEnum, name="candidate_status"),
        nullable=False,
        default=StatusEnum.applied,
    )
