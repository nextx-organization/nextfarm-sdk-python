from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeSaveTaskFilterRequest")



@_attrs_define
class OfficeSaveTaskFilterRequest:
    

    is_shared: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    payload: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_shared = self.is_shared

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_shared is not UNSET:
            field_dict["isShared"] = is_shared
        if name is not UNSET:
            field_dict["name"] = name
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_shared = d.pop("isShared", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))


        office_save_task_filter_request = cls(
            is_shared=is_shared,
            name=name,
            payload=payload,
        )

        return office_save_task_filter_request

