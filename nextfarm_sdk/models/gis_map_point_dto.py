from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisMapPointDto")



@_attrs_define
class GisMapPointDto:
    

    area_ha: float | None | Unset = UNSET
    farmer_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    kind: None | str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    name: None | str | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    parcel_count: int | None | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        area_ha: float | None | Unset
        if isinstance(self.area_ha, Unset):
            area_ha = UNSET
        else:
            area_ha = self.area_ha

        farmer_id: None | str | Unset
        if isinstance(self.farmer_id, Unset):
            farmer_id = UNSET
        elif isinstance(self.farmer_id, UUID):
            farmer_id = str(self.farmer_id)
        else:
            farmer_id = self.farmer_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        latitude = self.latitude

        longitude = self.longitude

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        parcel_count: int | None | Unset
        if isinstance(self.parcel_count, Unset):
            parcel_count = UNSET
        else:
            parcel_count = self.parcel_count

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if area_ha is not UNSET:
            field_dict["area_ha"] = area_ha
        if farmer_id is not UNSET:
            field_dict["farmer_id"] = farmer_id
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if parcel_count is not UNSET:
            field_dict["parcel_count"] = parcel_count
        if status is not UNSET:
            field_dict["status"] = status

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


        def _parse_farmer_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                farmer_id_type_0 = UUID(data)



                return farmer_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        farmer_id = _parse_farmer_id(d.pop("farmer_id", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcel_code", UNSET))


        def _parse_parcel_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parcel_count = _parse_parcel_count(d.pop("parcel_count", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        gis_map_point_dto = cls(
            area_ha=area_ha,
            farmer_id=farmer_id,
            id=id,
            kind=kind,
            latitude=latitude,
            longitude=longitude,
            name=name,
            parcel_code=parcel_code,
            parcel_count=parcel_count,
            status=status,
        )

        return gis_map_point_dto

