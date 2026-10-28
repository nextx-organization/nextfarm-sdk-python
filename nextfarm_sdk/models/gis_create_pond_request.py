from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisCreatePondRequest")



@_attrs_define
class GisCreatePondRequest:
    

    area_ha: float | Unset = UNSET
    boundary_geo_json: None | str | Unset = UNSET
    depth_m: float | None | Unset = UNSET
    metadata: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    pond_code: None | str | Unset = UNSET
    pond_type: None | str | Unset = UNSET
    salinity_ppt: float | None | Unset = UNSET
    source_parcel_id: None | Unset | UUID = UNSET
    volume_m3: float | None | Unset = UNSET
    water_source: None | str | Unset = UNSET
    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        area_ha = self.area_ha

        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json

        depth_m: float | None | Unset
        if isinstance(self.depth_m, Unset):
            depth_m = UNSET
        else:
            depth_m = self.depth_m

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

        pond_code: None | str | Unset
        if isinstance(self.pond_code, Unset):
            pond_code = UNSET
        else:
            pond_code = self.pond_code

        pond_type: None | str | Unset
        if isinstance(self.pond_type, Unset):
            pond_type = UNSET
        else:
            pond_type = self.pond_type

        salinity_ppt: float | None | Unset
        if isinstance(self.salinity_ppt, Unset):
            salinity_ppt = UNSET
        else:
            salinity_ppt = self.salinity_ppt

        source_parcel_id: None | str | Unset
        if isinstance(self.source_parcel_id, Unset):
            source_parcel_id = UNSET
        elif isinstance(self.source_parcel_id, UUID):
            source_parcel_id = str(self.source_parcel_id)
        else:
            source_parcel_id = self.source_parcel_id

        volume_m3: float | None | Unset
        if isinstance(self.volume_m3, Unset):
            volume_m3 = UNSET
        else:
            volume_m3 = self.volume_m3

        water_source: None | str | Unset
        if isinstance(self.water_source, Unset):
            water_source = UNSET
        else:
            water_source = self.water_source

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
        if depth_m is not UNSET:
            field_dict["depth_m"] = depth_m
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if pond_code is not UNSET:
            field_dict["pond_code"] = pond_code
        if pond_type is not UNSET:
            field_dict["pond_type"] = pond_type
        if salinity_ppt is not UNSET:
            field_dict["salinity_ppt"] = salinity_ppt
        if source_parcel_id is not UNSET:
            field_dict["source_parcel_id"] = source_parcel_id
        if volume_m3 is not UNSET:
            field_dict["volume_m3"] = volume_m3
        if water_source is not UNSET:
            field_dict["water_source"] = water_source
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        area_ha = d.pop("area_ha", UNSET)

        def _parse_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_geo_json = _parse_boundary_geo_json(d.pop("boundary_geo_json", UNSET))


        def _parse_depth_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_m = _parse_depth_m(d.pop("depth_m", UNSET))


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


        def _parse_pond_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pond_code = _parse_pond_code(d.pop("pond_code", UNSET))


        def _parse_pond_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pond_type = _parse_pond_type(d.pop("pond_type", UNSET))


        def _parse_salinity_ppt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        salinity_ppt = _parse_salinity_ppt(d.pop("salinity_ppt", UNSET))


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


        def _parse_volume_m3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        volume_m3 = _parse_volume_m3(d.pop("volume_m3", UNSET))


        def _parse_water_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_source = _parse_water_source(d.pop("water_source", UNSET))


        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        gis_create_pond_request = cls(
            area_ha=area_ha,
            boundary_geo_json=boundary_geo_json,
            depth_m=depth_m,
            metadata=metadata,
            name=name,
            pond_code=pond_code,
            pond_type=pond_type,
            salinity_ppt=salinity_ppt,
            source_parcel_id=source_parcel_id,
            volume_m3=volume_m3,
            water_source=water_source,
            zone_id=zone_id,
        )

        return gis_create_pond_request

