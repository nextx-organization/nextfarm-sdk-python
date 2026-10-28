from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotChannelManualMaxMinRequest")



@_attrs_define
class IotChannelManualMaxMinRequest:
    

    idx: int | Unset = UNSET
    manual_max_min: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        idx = self.idx

        manual_max_min: int | None | Unset
        if isinstance(self.manual_max_min, Unset):
            manual_max_min = UNSET
        else:
            manual_max_min = self.manual_max_min


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if idx is not UNSET:
            field_dict["idx"] = idx
        if manual_max_min is not UNSET:
            field_dict["manual_max_min"] = manual_max_min

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idx = d.pop("idx", UNSET)

        def _parse_manual_max_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        manual_max_min = _parse_manual_max_min(d.pop("manual_max_min", UNSET))


        iot_channel_manual_max_min_request = cls(
            idx=idx,
            manual_max_min=manual_max_min,
        )

        return iot_channel_manual_max_min_request

