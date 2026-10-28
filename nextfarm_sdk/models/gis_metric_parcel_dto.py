from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="GisMetricParcelDto")



@_attrs_define
class GisMetricParcelDto:
    

    area_ha: float | Unset = UNSET
    parcel_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        area_ha = self.area_ha

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if area_ha is not UNSET:
            field_dict["area_ha"] = area_ha
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        area_ha = d.pop("area_ha", UNSET)

        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        gis_metric_parcel_dto = cls(
            area_ha=area_ha,
            parcel_id=parcel_id,
        )

        return gis_metric_parcel_dto

