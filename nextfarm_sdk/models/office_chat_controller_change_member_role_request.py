from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerChangeMemberRoleRequest")



@_attrs_define
class OfficeChatControllerChangeMemberRoleRequest:
    

    role: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        office_chat_controller_change_member_role_request = cls(
            role=role,
        )

        return office_chat_controller_change_member_role_request

