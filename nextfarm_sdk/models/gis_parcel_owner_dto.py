from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisParcelOwnerDto")



@_attrs_define
class GisParcelOwnerDto:
    

    full_name: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    phone: None | str | Unset = UNSET
    public_name_consent: bool | Unset = UNSET
    public_phone_consent: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        public_name_consent = self.public_name_consent

        public_phone_consent = self.public_phone_consent


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if public_name_consent is not UNSET:
            field_dict["public_name_consent"] = public_name_consent
        if public_phone_consent is not UNSET:
            field_dict["public_phone_consent"] = public_phone_consent

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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        public_name_consent = d.pop("public_name_consent", UNSET)

        public_phone_consent = d.pop("public_phone_consent", UNSET)

        gis_parcel_owner_dto = cls(
            full_name=full_name,
            id=id,
            phone=phone,
            public_name_consent=public_name_consent,
            public_phone_consent=public_phone_consent,
        )

        return gis_parcel_owner_dto

