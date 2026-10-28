from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="HarvestCertGroupInput")



@_attrs_define
class HarvestCertGroupInput:
    

    certificate_number: None | str | Unset = UNSET
    expires_on: datetime.date | None | Unset = UNSET
    issued_by: None | str | Unset = UNSET
    issued_on: datetime.date | None | Unset = UNSET
    name: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    scheme: None | str | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        certificate_number: None | str | Unset
        if isinstance(self.certificate_number, Unset):
            certificate_number = UNSET
        else:
            certificate_number = self.certificate_number

        expires_on: None | str | Unset
        if isinstance(self.expires_on, Unset):
            expires_on = UNSET
        elif isinstance(self.expires_on, datetime.date):
            expires_on = self.expires_on.isoformat()
        else:
            expires_on = self.expires_on

        issued_by: None | str | Unset
        if isinstance(self.issued_by, Unset):
            issued_by = UNSET
        else:
            issued_by = self.issued_by

        issued_on: None | str | Unset
        if isinstance(self.issued_on, Unset):
            issued_on = UNSET
        elif isinstance(self.issued_on, datetime.date):
            issued_on = self.issued_on.isoformat()
        else:
            issued_on = self.issued_on

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        scheme: None | str | Unset
        if isinstance(self.scheme, Unset):
            scheme = UNSET
        else:
            scheme = self.scheme

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if certificate_number is not UNSET:
            field_dict["certificate_number"] = certificate_number
        if expires_on is not UNSET:
            field_dict["expires_on"] = expires_on
        if issued_by is not UNSET:
            field_dict["issued_by"] = issued_by
        if issued_on is not UNSET:
            field_dict["issued_on"] = issued_on
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if status is not UNSET:
            field_dict["status"] = status

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


        def _parse_expires_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_on_type_0 = datetime.date.fromisoformat(data)



                return expires_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expires_on = _parse_expires_on(d.pop("expires_on", UNSET))


        def _parse_issued_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issued_by = _parse_issued_by(d.pop("issued_by", UNSET))


        def _parse_issued_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issued_on_type_0 = datetime.date.fromisoformat(data)



                return issued_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        issued_on = _parse_issued_on(d.pop("issued_on", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_scheme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme = _parse_scheme(d.pop("scheme", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        harvest_cert_group_input = cls(
            certificate_number=certificate_number,
            expires_on=expires_on,
            issued_by=issued_by,
            issued_on=issued_on,
            name=name,
            note=note,
            scheme=scheme,
            status=status,
        )

        return harvest_cert_group_input

