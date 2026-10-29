from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisCreateFacilityRequest")



@_attrs_define
class GisCreateFacilityRequest:
    

    area_ha: float | None | Unset = UNSET
    boundary_geo_json: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    capacity: int | None | Unset = UNSET
    facility_code: None | str | Unset = UNSET
    facility_type: None | str | Unset = UNSET
    metadata: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    source_parcel_id: None | Unset | UUID = UNSET
    zone_id: UUID | Unset = UNSET





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

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        capacity: int | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

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

        metadata: None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

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

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if area_ha is not UNSET:
            field_dict["area_ha"] = area_ha
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if facility_code is not UNSET:
            field_dict["facility_code"] = facility_code
        if facility_type is not UNSET:
            field_dict["facility_type"] = facility_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if source_parcel_id is not UNSET:
            field_dict["source_parcel_id"] = source_parcel_id
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

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


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branch_id", UNSET))


        def _parse_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))


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


        def _parse_metadata(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


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


        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        gis_create_facility_request = cls(
            area_ha=area_ha,
            boundary_geo_json=boundary_geo_json,
            branch_id=branch_id,
            capacity=capacity,
            facility_code=facility_code,
            facility_type=facility_type,
            metadata=metadata,
            name=name,
            source_parcel_id=source_parcel_id,
            zone_id=zone_id,
        )

        return gis_create_facility_request

