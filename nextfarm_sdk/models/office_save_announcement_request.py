from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeSaveAnnouncementRequest")



@_attrs_define
class OfficeSaveAnnouncementRequest:
    

    saved: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        saved = self.saved


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if saved is not UNSET:
            field_dict["saved"] = saved

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        saved = d.pop("saved", UNSET)

        office_save_announcement_request = cls(
            saved=saved,
        )

        return office_save_announcement_request

