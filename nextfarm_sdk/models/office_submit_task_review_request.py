from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeSubmitTaskReviewRequest")



@_attrs_define
class OfficeSubmitTaskReviewRequest:
    

    result_note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        result_note: None | str | Unset
        if isinstance(self.result_note, Unset):
            result_note = UNSET
        else:
            result_note = self.result_note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if result_note is not UNSET:
            field_dict["resultNote"] = result_note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_result_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_note = _parse_result_note(d.pop("resultNote", UNSET))


        office_submit_task_review_request = cls(
            result_note=result_note,
        )

        return office_submit_task_review_request

