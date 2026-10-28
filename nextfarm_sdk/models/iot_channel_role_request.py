from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotChannelRoleRequest")



@_attrs_define
class IotChannelRoleRequest:
    

    idx: int | Unset = UNSET
    role: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        idx = self.idx

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if idx is not UNSET:
            field_dict["idx"] = idx
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idx = d.pop("idx", UNSET)

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        iot_channel_role_request = cls(
            idx=idx,
            role=role,
        )

        return iot_channel_role_request

