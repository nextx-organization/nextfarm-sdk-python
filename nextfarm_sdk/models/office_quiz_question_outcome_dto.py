from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeQuizQuestionOutcomeDto")



@_attrs_define
class OfficeQuizQuestionOutcomeDto:
    

    answered_correctly: bool | Unset = UNSET
    question_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        answered_correctly = self.answered_correctly

        question_id: str | Unset = UNSET
        if not isinstance(self.question_id, Unset):
            question_id = str(self.question_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if answered_correctly is not UNSET:
            field_dict["answeredCorrectly"] = answered_correctly
        if question_id is not UNSET:
            field_dict["questionId"] = question_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        answered_correctly = d.pop("answeredCorrectly", UNSET)

        _question_id = d.pop("questionId", UNSET)
        question_id: UUID | Unset
        if isinstance(_question_id,  Unset):
            question_id = UNSET
        else:
            question_id = UUID(_question_id)




        office_quiz_question_outcome_dto = cls(
            answered_correctly=answered_correctly,
            question_id=question_id,
        )

        return office_quiz_question_outcome_dto

