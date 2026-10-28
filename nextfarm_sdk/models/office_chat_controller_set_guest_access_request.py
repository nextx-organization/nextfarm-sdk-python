from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeChatControllerSetGuestAccessRequest")



@_attrs_define
class OfficeChatControllerSetGuestAccessRequest:
    

    allow_guests: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allow_guests = self.allow_guests


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allow_guests is not UNSET:
            field_dict["allowGuests"] = allow_guests

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_guests = d.pop("allowGuests", UNSET)

        office_chat_controller_set_guest_access_request = cls(
            allow_guests=allow_guests,
        )

        return office_chat_controller_set_guest_access_request

