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






T = TypeVar("T", bound="GisFarmerDto")



@_attrs_define
class GisFarmerDto:
    

    address: None | str | Unset = UNSET
    cooperative_name: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    full_name: None | str | Unset = UNSET
    group_id: None | Unset | UUID = UNSET
    group_name: None | str | Unset = UNSET
    home_location_geo_json: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    identity_number: None | str | Unset = UNSET
    member_type: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    public_consent_at: datetime.datetime | None | Unset = UNSET
    public_consent_by: None | Unset | UUID = UNSET
    public_name_consent: bool | Unset = UNSET
    public_phone_consent: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET
    zone_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        cooperative_name: None | str | Unset
        if isinstance(self.cooperative_name, Unset):
            cooperative_name = UNSET
        else:
            cooperative_name = self.cooperative_name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        home_location_geo_json: None | str | Unset
        if isinstance(self.home_location_geo_json, Unset):
            home_location_geo_json = UNSET
        else:
            home_location_geo_json = self.home_location_geo_json

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        identity_number: None | str | Unset
        if isinstance(self.identity_number, Unset):
            identity_number = UNSET
        else:
            identity_number = self.identity_number

        member_type: None | str | Unset
        if isinstance(self.member_type, Unset):
            member_type = UNSET
        else:
            member_type = self.member_type

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        public_consent_at: None | str | Unset
        if isinstance(self.public_consent_at, Unset):
            public_consent_at = UNSET
        elif isinstance(self.public_consent_at, datetime.datetime):
            public_consent_at = self.public_consent_at.isoformat()
        else:
            public_consent_at = self.public_consent_at

        public_consent_by: None | str | Unset
        if isinstance(self.public_consent_by, Unset):
            public_consent_by = UNSET
        elif isinstance(self.public_consent_by, UUID):
            public_consent_by = str(self.public_consent_by)
        else:
            public_consent_by = self.public_consent_by

        public_name_consent = self.public_name_consent

        public_phone_consent = self.public_phone_consent

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id

        zone_name: None | str | Unset
        if isinstance(self.zone_name, Unset):
            zone_name = UNSET
        else:
            zone_name = self.zone_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if cooperative_name is not UNSET:
            field_dict["cooperative_name"] = cooperative_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if home_location_geo_json is not UNSET:
            field_dict["home_location_geo_json"] = home_location_geo_json
        if id is not UNSET:
            field_dict["id"] = id
        if identity_number is not UNSET:
            field_dict["identity_number"] = identity_number
        if member_type is not UNSET:
            field_dict["member_type"] = member_type
        if phone is not UNSET:
            field_dict["phone"] = phone
        if public_consent_at is not UNSET:
            field_dict["public_consent_at"] = public_consent_at
        if public_consent_by is not UNSET:
            field_dict["public_consent_by"] = public_consent_by
        if public_name_consent is not UNSET:
            field_dict["public_name_consent"] = public_name_consent
        if public_phone_consent is not UNSET:
            field_dict["public_phone_consent"] = public_phone_consent
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if zone_name is not UNSET:
            field_dict["zone_name"] = zone_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_cooperative_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cooperative_name = _parse_cooperative_name(d.pop("cooperative_name", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))


        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)



                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))


        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("group_name", UNSET))


        def _parse_home_location_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_location_geo_json = _parse_home_location_geo_json(d.pop("home_location_geo_json", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_identity_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_number = _parse_identity_number(d.pop("identity_number", UNSET))


        def _parse_member_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_type = _parse_member_type(d.pop("member_type", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_public_consent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                public_consent_at_type_0 = datetime.datetime.fromisoformat(data)



                return public_consent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        public_consent_at = _parse_public_consent_at(d.pop("public_consent_at", UNSET))


        def _parse_public_consent_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                public_consent_by_type_0 = UUID(data)



                return public_consent_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        public_consent_by = _parse_public_consent_by(d.pop("public_consent_by", UNSET))


        public_name_consent = d.pop("public_name_consent", UNSET)

        public_phone_consent = d.pop("public_phone_consent", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




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


        def _parse_zone_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_name = _parse_zone_name(d.pop("zone_name", UNSET))


        gis_farmer_dto = cls(
            address=address,
            cooperative_name=cooperative_name,
            created_at=created_at,
            full_name=full_name,
            group_id=group_id,
            group_name=group_name,
            home_location_geo_json=home_location_geo_json,
            id=id,
            identity_number=identity_number,
            member_type=member_type,
            phone=phone,
            public_consent_at=public_consent_at,
            public_consent_by=public_consent_by,
            public_name_consent=public_name_consent,
            public_phone_consent=public_phone_consent,
            updated_at=updated_at,
            zone_id=zone_id,
            zone_name=zone_name,
        )

        return gis_farmer_dto

