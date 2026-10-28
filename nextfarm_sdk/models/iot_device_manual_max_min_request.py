from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IotDeviceManualMaxMinRequest")



@_attrs_define
class IotDeviceManualMaxMinRequest:
    

    manual_max_min: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        manual_max_min = self.manual_max_min


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if manual_max_min is not UNSET:
            field_dict["manual_max_min"] = manual_max_min

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manual_max_min = d.pop("manual_max_min", UNSET)

        iot_device_manual_max_min_request = cls(
            manual_max_min=manual_max_min,
        )

        return iot_device_manual_max_min_request

