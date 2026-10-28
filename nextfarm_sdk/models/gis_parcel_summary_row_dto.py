from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisParcelSummaryRowDto")



@_attrs_define
class GisParcelSummaryRowDto:
    

    estimated_area_ha: float | Unset = UNSET
    excluded_area_ha: float | Unset = UNSET
    farmer_count: int | Unset = UNSET
    implausible_count: int | Unset = UNSET
    key: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    parcel_count: int | Unset = UNSET
    parcels_without_boundary_count: int | Unset = UNSET
    total_area_ha: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        estimated_area_ha = self.estimated_area_ha

        excluded_area_ha = self.excluded_area_ha

        farmer_count = self.farmer_count

        implausible_count = self.implausible_count

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        elif isinstance(self.key, UUID):
            key = str(self.key)
        else:
            key = self.key

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parcel_count = self.parcel_count

        parcels_without_boundary_count = self.parcels_without_boundary_count

        total_area_ha = self.total_area_ha


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if estimated_area_ha is not UNSET:
            field_dict["estimated_area_ha"] = estimated_area_ha
        if excluded_area_ha is not UNSET:
            field_dict["excluded_area_ha"] = excluded_area_ha
        if farmer_count is not UNSET:
            field_dict["farmer_count"] = farmer_count
        if implausible_count is not UNSET:
            field_dict["implausible_count"] = implausible_count
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_count is not UNSET:
            field_dict["parcel_count"] = parcel_count
        if parcels_without_boundary_count is not UNSET:
            field_dict["parcels_without_boundary_count"] = parcels_without_boundary_count
        if total_area_ha is not UNSET:
            field_dict["total_area_ha"] = total_area_ha

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        estimated_area_ha = d.pop("estimated_area_ha", UNSET)

        excluded_area_ha = d.pop("excluded_area_ha", UNSET)

        farmer_count = d.pop("farmer_count", UNSET)

        implausible_count = d.pop("implausible_count", UNSET)

        def _parse_key(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                key_type_0 = UUID(data)



                return key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        parcel_count = d.pop("parcel_count", UNSET)

        parcels_without_boundary_count = d.pop("parcels_without_boundary_count", UNSET)

        total_area_ha = d.pop("total_area_ha", UNSET)

        gis_parcel_summary_row_dto = cls(
            estimated_area_ha=estimated_area_ha,
            excluded_area_ha=excluded_area_ha,
            farmer_count=farmer_count,
            implausible_count=implausible_count,
            key=key,
            name=name,
            parcel_count=parcel_count,
            parcels_without_boundary_count=parcels_without_boundary_count,
            total_area_ha=total_area_ha,
        )

        return gis_parcel_summary_row_dto

