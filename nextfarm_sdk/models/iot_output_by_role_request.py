from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotOutputByRoleRequest")



@_attrs_define
class IotOutputByRoleRequest:
    

    idx: int | None | Unset = UNSET
    on: bool | None | Unset = UNSET
    role: None | str | Unset = UNSET
    value: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        idx: int | None | Unset
        if isinstance(self.idx, Unset):
            idx = UNSET
        else:
            idx = self.idx

        on: bool | None | Unset
        if isinstance(self.on, Unset):
            on = UNSET
        else:
            on = self.on

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        value: int | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if idx is not UNSET:
            field_dict["idx"] = idx
        if on is not UNSET:
            field_dict["on"] = on
        if role is not UNSET:
            field_dict["role"] = role
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_idx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idx = _parse_idx(d.pop("idx", UNSET))


        def _parse_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        on = _parse_on(d.pop("on", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        def _parse_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        iot_output_by_role_request = cls(
            idx=idx,
            on=on,
            role=role,
            value=value,
        )

        return iot_output_by_role_request

