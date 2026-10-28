from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeForwardMessageResultDto")



@_attrs_define
class OfficeForwardMessageResultDto:
    

    forwarded_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        forwarded_count = self.forwarded_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if forwarded_count is not UNSET:
            field_dict["forwardedCount"] = forwarded_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forwarded_count = d.pop("forwardedCount", UNSET)

        office_forward_message_result_dto = cls(
            forwarded_count=forwarded_count,
        )

        return office_forward_message_result_dto

