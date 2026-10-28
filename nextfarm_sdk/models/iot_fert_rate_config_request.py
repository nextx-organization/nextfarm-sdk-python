from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IotFertRateConfigRequest")



@_attrs_define
class IotFertRateConfigRequest:
    

    idx: int | Unset = UNSET
    rate: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        idx = self.idx

        rate = self.rate


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if idx is not UNSET:
            field_dict["idx"] = idx
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idx = d.pop("idx", UNSET)

        rate = d.pop("rate", UNSET)

        iot_fert_rate_config_request = cls(
            idx=idx,
            rate=rate,
        )

        return iot_fert_rate_config_request

