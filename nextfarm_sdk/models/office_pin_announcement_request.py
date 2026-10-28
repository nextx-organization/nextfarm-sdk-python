from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficePinAnnouncementRequest")



@_attrs_define
class OfficePinAnnouncementRequest:
    

    pinned: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        pinned = self.pinned


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if pinned is not UNSET:
            field_dict["pinned"] = pinned

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pinned = d.pop("pinned", UNSET)

        office_pin_announcement_request = cls(
            pinned=pinned,
        )

        return office_pin_announcement_request

