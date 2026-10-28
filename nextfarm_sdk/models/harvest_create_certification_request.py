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






T = TypeVar("T", bound="HarvestCreateCertificationRequest")



@_attrs_define
class HarvestCreateCertificationRequest:
    

    certificate_number: None | str | Unset = UNSET
    expiry_date: datetime.date | Unset = UNSET
    issued_by: None | str | Unset = UNSET
    issued_date: datetime.date | Unset = UNSET
    name: None | str | Unset = UNSET
    parcel_id: None | Unset | UUID = UNSET
    scheme: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        certificate_number: None | str | Unset
        if isinstance(self.certificate_number, Unset):
            certificate_number = UNSET
        else:
            certificate_number = self.certificate_number

        expiry_date: str | Unset = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        issued_by: None | str | Unset
        if isinstance(self.issued_by, Unset):
            issued_by = UNSET
        else:
            issued_by = self.issued_by

        issued_date: str | Unset = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parcel_id: None | str | Unset
        if isinstance(self.parcel_id, Unset):
            parcel_id = UNSET
        elif isinstance(self.parcel_id, UUID):
            parcel_id = str(self.parcel_id)
        else:
            parcel_id = self.parcel_id

        scheme: None | str | Unset
        if isinstance(self.scheme, Unset):
            scheme = UNSET
        else:
            scheme = self.scheme


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if certificate_number is not UNSET:
            field_dict["certificate_number"] = certificate_number
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if issued_by is not UNSET:
            field_dict["issued_by"] = issued_by
        if issued_date is not UNSET:
            field_dict["issued_date"] = issued_date
        if name is not UNSET:
            field_dict["name"] = name
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if scheme is not UNSET:
            field_dict["scheme"] = scheme

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_certificate_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certificate_number = _parse_certificate_number(d.pop("certificate_number", UNSET))


        _expiry_date = d.pop("expiry_date", UNSET)
        expiry_date: datetime.date | Unset
        if isinstance(_expiry_date,  Unset):
            expiry_date = UNSET
        else:
            expiry_date = datetime.date.fromisoformat(_expiry_date)




        def _parse_issued_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issued_by = _parse_issued_by(d.pop("issued_by", UNSET))


        _issued_date = d.pop("issued_date", UNSET)
        issued_date: datetime.date | Unset
        if isinstance(_issued_date,  Unset):
            issued_date = UNSET
        else:
            issued_date = datetime.date.fromisoformat(_issued_date)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_parcel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parcel_id_type_0 = UUID(data)



                return parcel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parcel_id = _parse_parcel_id(d.pop("parcel_id", UNSET))


        def _parse_scheme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme = _parse_scheme(d.pop("scheme", UNSET))


        harvest_create_certification_request = cls(
            certificate_number=certificate_number,
            expiry_date=expiry_date,
            issued_by=issued_by,
            issued_date=issued_date,
            name=name,
            parcel_id=parcel_id,
            scheme=scheme,
        )

        return harvest_create_certification_request

