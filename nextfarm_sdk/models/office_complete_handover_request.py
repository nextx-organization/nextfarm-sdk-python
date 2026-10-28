from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeCompleteHandoverRequest")



@_attrs_define
class OfficeCompleteHandoverRequest:
    

    approved: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        approved = self.approved


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if approved is not UNSET:
            field_dict["approved"] = approved

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approved = d.pop("approved", UNSET)

        office_complete_handover_request = cls(
            approved=approved,
        )

        return office_complete_handover_request

