from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeDirectoryControllerResolveEmailsRequest")



@_attrs_define
class OfficeDirectoryControllerResolveEmailsRequest:
    

    emails: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        emails: list[str] | None | Unset
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = self.emails


        else:
            emails = self.emails


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if emails is not UNSET:
            field_dict["emails"] = emails

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = cast(list[str], data)

                return emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        emails = _parse_emails(d.pop("emails", UNSET))


        office_directory_controller_resolve_emails_request = cls(
            emails=emails,
        )

        return office_directory_controller_resolve_emails_request

