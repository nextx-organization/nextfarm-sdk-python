from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="GisFacilityListItemDto")



@_attrs_define
class GisFacilityListItemDto:
    

    area_ha: float | None | Unset = UNSET
    boundary_geo_json: None | str | Unset = UNSET
    capacity: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    current_stock: int | Unset = UNSET
    facility_code: None | str | Unset = UNSET
    facility_type: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    source_parcel_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    zone_id: UUID | Unset = UNSET
    zone_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        area_ha: float | None | Unset
        if isinstance(self.area_ha, Unset):
            area_ha = UNSET
        else:
            area_ha = self.area_ha

        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json

        capacity: int | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        current_stock = self.current_stock

        facility_code: None | str | Unset
        if isinstance(self.facility_code, Unset):
            facility_code = UNSET
        else:
            facility_code = self.facility_code

        facility_type: None | str | Unset
        if isinstance(self.facility_type, Unset):
            facility_type = UNSET
        else:
            facility_type = self.facility_type

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source_parcel_id: None | str | Unset
        if isinstance(self.source_parcel_id, Unset):
            source_parcel_id = UNSET
        elif isinstance(self.source_parcel_id, UUID):
            source_parcel_id = str(self.source_parcel_id)
        else:
            source_parcel_id = self.source_parcel_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

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
        if area_ha is not UNSET:
            field_dict["area_ha"] = area_ha
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if current_stock is not UNSET:
            field_dict["current_stock"] = current_stock
        if facility_code is not UNSET:
            field_dict["facility_code"] = facility_code
        if facility_type is not UNSET:
            field_dict["facility_type"] = facility_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if source_parcel_id is not UNSET:
            field_dict["source_parcel_id"] = source_parcel_id
        if status is not UNSET:
            field_dict["status"] = status
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if zone_name is not UNSET:
            field_dict["zone_name"] = zone_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_area_ha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area_ha = _parse_area_ha(d.pop("area_ha", UNSET))


        def _parse_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_geo_json = _parse_boundary_geo_json(d.pop("boundary_geo_json", UNSET))


        def _parse_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        current_stock = d.pop("current_stock", UNSET)

        def _parse_facility_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_code = _parse_facility_code(d.pop("facility_code", UNSET))


        def _parse_facility_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_type = _parse_facility_type(d.pop("facility_type", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_source_parcel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_parcel_id_type_0 = UUID(data)



                return source_parcel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_parcel_id = _parse_source_parcel_id(d.pop("source_parcel_id", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


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


        gis_facility_list_item_dto = cls(
            area_ha=area_ha,
            boundary_geo_json=boundary_geo_json,
            capacity=capacity,
            created_at=created_at,
            current_stock=current_stock,
            facility_code=facility_code,
            facility_type=facility_type,
            id=id,
            name=name,
            source_parcel_id=source_parcel_id,
            status=status,
            zone_id=zone_id,
            zone_name=zone_name,
        )

        return gis_facility_list_item_dto

