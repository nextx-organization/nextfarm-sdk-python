from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IotFertTargetConfigRequest")



@_attrs_define
class IotFertTargetConfigRequest:
    

    idx: int | Unset = UNSET
    ml: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        idx = self.idx

        ml = self.ml


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if idx is not UNSET:
            field_dict["idx"] = idx
        if ml is not UNSET:
            field_dict["ml"] = ml

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idx = d.pop("idx", UNSET)

        ml = d.pop("ml", UNSET)

        iot_fert_target_config_request = cls(
            idx=idx,
            ml=ml,
        )

        return iot_fert_target_config_request

