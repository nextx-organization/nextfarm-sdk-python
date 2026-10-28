from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeQuizAttemptSummaryDto")



@_attrs_define
class OfficeQuizAttemptSummaryDto:
    

    attempt_no: int | Unset = UNSET
    passed: bool | Unset = UNSET
    score_percent: int | Unset = UNSET
    submitted_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        attempt_no = self.attempt_no

        passed = self.passed

        score_percent = self.score_percent

        submitted_at: str | Unset = UNSET
        if not isinstance(self.submitted_at, Unset):
            submitted_at = self.submitted_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attempt_no is not UNSET:
            field_dict["attemptNo"] = attempt_no
        if passed is not UNSET:
            field_dict["passed"] = passed
        if score_percent is not UNSET:
            field_dict["scorePercent"] = score_percent
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_no = d.pop("attemptNo", UNSET)

        passed = d.pop("passed", UNSET)

        score_percent = d.pop("scorePercent", UNSET)

        _submitted_at = d.pop("submittedAt", UNSET)
        submitted_at: datetime.datetime | Unset
        if isinstance(_submitted_at,  Unset):
            submitted_at = UNSET
        else:
            submitted_at = datetime.datetime.fromisoformat(_submitted_at)




        office_quiz_attempt_summary_dto = cls(
            attempt_no=attempt_no,
            passed=passed,
            score_percent=score_percent,
            submitted_at=submitted_at,
        )

        return office_quiz_attempt_summary_dto

