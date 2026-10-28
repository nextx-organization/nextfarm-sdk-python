from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeReviewScoreInput")



@_attrs_define
class OfficeReviewScoreInput:
    

    comment: None | str | Unset = UNSET
    criterion_id: UUID | Unset = UNSET
    score: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        criterion_id: str | Unset = UNSET
        if not isinstance(self.criterion_id, Unset):
            criterion_id = str(self.criterion_id)

        score: int | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if comment is not UNSET:
            field_dict["comment"] = comment
        if criterion_id is not UNSET:
            field_dict["criterionId"] = criterion_id
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        _criterion_id = d.pop("criterionId", UNSET)
        criterion_id: UUID | Unset
        if isinstance(_criterion_id,  Unset):
            criterion_id = UNSET
        else:
            criterion_id = UUID(_criterion_id)




        def _parse_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))


        office_review_score_input = cls(
            comment=comment,
            criterion_id=criterion_id,
            score=score,
        )

        return office_review_score_input

