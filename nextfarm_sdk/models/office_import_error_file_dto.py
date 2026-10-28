from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeImportErrorFileDto")



@_attrs_define
class OfficeImportErrorFileDto:
    

    error_file_url: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error_file_url: None | str | Unset
        if isinstance(self.error_file_url, Unset):
            error_file_url = UNSET
        else:
            error_file_url = self.error_file_url

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if error_file_url is not UNSET:
            field_dict["errorFileUrl"] = error_file_url
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_error_file_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_file_url = _parse_error_file_url(d.pop("errorFileUrl", UNSET))


        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        office_import_error_file_dto = cls(
            error_file_url=error_file_url,
            expires_at=expires_at,
        )

        return office_import_error_file_dto

