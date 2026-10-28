from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisZoneStatsDto")



@_attrs_define
class GisZoneStatsDto:
    

    active_parcel_count: int | Unset = UNSET
    disputed_parcel_count: int | Unset = UNSET
    excluded_area_ha: float | Unset = UNSET
    implausible_parcel_count: int | Unset = UNSET
    inactive_parcel_count: int | Unset = UNSET
    parcel_count: int | Unset = UNSET
    total_area_ha: float | Unset = UNSET
    zone_id: UUID | Unset = UNSET
    zone_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        active_parcel_count = self.active_parcel_count

        disputed_parcel_count = self.disputed_parcel_count

        excluded_area_ha = self.excluded_area_ha

        implausible_parcel_count = self.implausible_parcel_count

        inactive_parcel_count = self.inactive_parcel_count

        parcel_count = self.parcel_count

        total_area_ha = self.total_area_ha

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)

        zone_name: None | str | Unset
        if isinstance(self.zone_name, Unset):
            zone_name = UNSET
        else:
            zone_name = self.zone_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active_parcel_count is not UNSET:
            field_dict["active_parcel_count"] = active_parcel_count
        if disputed_parcel_count is not UNSET:
            field_dict["disputed_parcel_count"] = disputed_parcel_count
        if excluded_area_ha is not UNSET:
            field_dict["excluded_area_ha"] = excluded_area_ha
        if implausible_parcel_count is not UNSET:
            field_dict["implausible_parcel_count"] = implausible_parcel_count
        if inactive_parcel_count is not UNSET:
            field_dict["inactive_parcel_count"] = inactive_parcel_count
        if parcel_count is not UNSET:
            field_dict["parcel_count"] = parcel_count
        if total_area_ha is not UNSET:
            field_dict["total_area_ha"] = total_area_ha
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if zone_name is not UNSET:
            field_dict["zone_name"] = zone_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_parcel_count = d.pop("active_parcel_count", UNSET)

        disputed_parcel_count = d.pop("disputed_parcel_count", UNSET)

        excluded_area_ha = d.pop("excluded_area_ha", UNSET)

        implausible_parcel_count = d.pop("implausible_parcel_count", UNSET)

        inactive_parcel_count = d.pop("inactive_parcel_count", UNSET)

        parcel_count = d.pop("parcel_count", UNSET)

        total_area_ha = d.pop("total_area_ha", UNSET)

        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        def _parse_zone_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_name = _parse_zone_name(d.pop("zone_name", UNSET))


        gis_zone_stats_dto = cls(
            active_parcel_count=active_parcel_count,
            disputed_parcel_count=disputed_parcel_count,
            excluded_area_ha=excluded_area_ha,
            implausible_parcel_count=implausible_parcel_count,
            inactive_parcel_count=inactive_parcel_count,
            parcel_count=parcel_count,
            total_area_ha=total_area_ha,
            zone_id=zone_id,
            zone_name=zone_name,
        )

        return gis_zone_stats_dto

