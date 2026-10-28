from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeReviewFormSummaryDto")



@_attrs_define
class OfficeReviewFormSummaryDto:
    

    awaiting_manager_review: int | Unset = UNSET
    awaiting_self_review: int | Unset = UNSET
    finalized: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        awaiting_manager_review = self.awaiting_manager_review

        awaiting_self_review = self.awaiting_self_review

        finalized = self.finalized

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if awaiting_manager_review is not UNSET:
            field_dict["awaitingManagerReview"] = awaiting_manager_review
        if awaiting_self_review is not UNSET:
            field_dict["awaitingSelfReview"] = awaiting_self_review
        if finalized is not UNSET:
            field_dict["finalized"] = finalized
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        awaiting_manager_review = d.pop("awaitingManagerReview", UNSET)

        awaiting_self_review = d.pop("awaitingSelfReview", UNSET)

        finalized = d.pop("finalized", UNSET)

        total = d.pop("total", UNSET)

        office_review_form_summary_dto = cls(
            awaiting_manager_review=awaiting_manager_review,
            awaiting_self_review=awaiting_self_review,
            finalized=finalized,
            total=total,
        )

        return office_review_form_summary_dto

