from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IotSetFertMeterInputRequest")



@_attrs_define
class IotSetFertMeterInputRequest:
    

    in_: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        in_ = self.in_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if in_ is not UNSET:
            field_dict["in"] = in_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_ = d.pop("in", UNSET)

        iot_set_fert_meter_input_request = cls(
            in_=in_,
        )

        return iot_set_fert_meter_input_request

