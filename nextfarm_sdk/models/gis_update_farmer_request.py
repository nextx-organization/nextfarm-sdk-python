from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisUpdateFarmerRequest")



@_attrs_define
class GisUpdateFarmerRequest:
    

    full_name: None | str | Unset = UNSET
    home_location_geo_json: None | str | Unset = UNSET
    identity_number: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        home_location_geo_json: None | str | Unset
        if isinstance(self.home_location_geo_json, Unset):
            home_location_geo_json = UNSET
        else:
            home_location_geo_json = self.home_location_geo_json

        identity_number: None | str | Unset
        if isinstance(self.identity_number, Unset):
            identity_number = UNSET
        else:
            identity_number = self.identity_number

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if home_location_geo_json is not UNSET:
            field_dict["home_location_geo_json"] = home_location_geo_json
        if identity_number is not UNSET:
            field_dict["identity_number"] = identity_number
        if phone is not UNSET:
            field_dict["phone"] = phone
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))


        def _parse_home_location_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_location_geo_json = _parse_home_location_geo_json(d.pop("home_location_geo_json", UNSET))


        def _parse_identity_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_number = _parse_identity_number(d.pop("identity_number", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)



                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zone_id", UNSET))


        gis_update_farmer_request = cls(
            full_name=full_name,
            home_location_geo_json=home_location_geo_json,
            identity_number=identity_number,
            phone=phone,
            zone_id=zone_id,
        )

        return gis_update_farmer_request

