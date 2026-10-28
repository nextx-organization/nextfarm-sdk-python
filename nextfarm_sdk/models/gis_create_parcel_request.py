from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisCreateParcelRequest")



@_attrs_define
class GisCreateParcelRequest:
    

    boundary_geo_json: None | str | Unset = UNSET
    crop_type_id: None | Unset | UUID = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    owner_id: None | Unset | UUID = UNSET
    parcel_code: None | str | Unset = UNSET
    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        boundary_geo_json: None | str | Unset
        if isinstance(self.boundary_geo_json, Unset):
            boundary_geo_json = UNSET
        else:
            boundary_geo_json = self.boundary_geo_json

        crop_type_id: None | str | Unset
        if isinstance(self.crop_type_id, Unset):
            crop_type_id = UNSET
        elif isinstance(self.crop_type_id, UUID):
            crop_type_id = str(self.crop_type_id)
        else:
            crop_type_id = self.crop_type_id

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        elif isinstance(self.owner_id, UUID):
            owner_id = str(self.owner_id)
        else:
            owner_id = self.owner_id

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if boundary_geo_json is not UNSET:
            field_dict["boundary_geo_json"] = boundary_geo_json
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_boundary_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary_geo_json = _parse_boundary_geo_json(d.pop("boundary_geo_json", UNSET))


        def _parse_crop_type_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                crop_type_id_type_0 = UUID(data)



                return crop_type_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        crop_type_id = _parse_crop_type_id(d.pop("crop_type_id", UNSET))


        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))


        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))


        def _parse_owner_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_id_type_0 = UUID(data)



                return owner_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))


        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcel_code", UNSET))


        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        gis_create_parcel_request = cls(
            boundary_geo_json=boundary_geo_json,
            crop_type_id=crop_type_id,
            latitude=latitude,
            longitude=longitude,
            owner_id=owner_id,
            parcel_code=parcel_code,
            zone_id=zone_id,
        )

        return gis_create_parcel_request

