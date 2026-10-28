from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotDeviceControlRequest")



@_attrs_define
class IotDeviceControlRequest:
    

    family: None | str | Unset = UNSET
    field: None | str | Unset = UNSET
    idx: int | None | Unset = UNSET
    index: int | None | Unset = UNSET
    type_: None | str | Unset = UNSET
    value: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        idx: int | None | Unset
        if isinstance(self.idx, Unset):
            idx = UNSET
        else:
            idx = self.idx

        index: int | None | Unset
        if isinstance(self.index, Unset):
            index = UNSET
        else:
            index = self.index

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if family is not UNSET:
            field_dict["family"] = family
        if field is not UNSET:
            field_dict["field"] = field
        if idx is not UNSET:
            field_dict["idx"] = idx
        if index is not UNSET:
            field_dict["index"] = index
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))


        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))


        def _parse_idx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idx = _parse_idx(d.pop("idx", UNSET))


        def _parse_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        index = _parse_index(d.pop("index", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        value = d.pop("value", UNSET)

        iot_device_control_request = cls(
            family=family,
            field=field,
            idx=idx,
            index=index,
            type_=type_,
            value=value,
        )

        return iot_device_control_request

