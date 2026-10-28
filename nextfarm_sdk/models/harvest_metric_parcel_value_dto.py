from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="HarvestMetricParcelValueDto")



@_attrs_define
class HarvestMetricParcelValueDto:
    

    parcel_id: UUID | Unset = UNSET
    value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        value = d.pop("value", UNSET)

        harvest_metric_parcel_value_dto = cls(
            parcel_id=parcel_id,
            value=value,
        )

        return harvest_metric_parcel_value_dto

