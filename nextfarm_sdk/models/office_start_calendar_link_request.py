from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeStartCalendarLinkRequest")



@_attrs_define
class OfficeStartCalendarLinkRequest:
    

    redirect_uri: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        redirect_uri: None | str | Unset
        if isinstance(self.redirect_uri, Unset):
            redirect_uri = UNSET
        else:
            redirect_uri = self.redirect_uri


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if redirect_uri is not UNSET:
            field_dict["redirectUri"] = redirect_uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_redirect_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_uri = _parse_redirect_uri(d.pop("redirectUri", UNSET))


        office_start_calendar_link_request = cls(
            redirect_uri=redirect_uri,
        )

        return office_start_calendar_link_request

