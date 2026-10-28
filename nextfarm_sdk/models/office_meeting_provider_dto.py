from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeMeetingProviderDto")



@_attrs_define
class OfficeMeetingProviderDto:
    

    code: None | str | Unset = UNSET
    connected: bool | Unset = UNSET
    link_from_calendar_event: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        connected = self.connected

        link_from_calendar_event = self.link_from_calendar_event


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if connected is not UNSET:
            field_dict["connected"] = connected
        if link_from_calendar_event is not UNSET:
            field_dict["linkFromCalendarEvent"] = link_from_calendar_event

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        connected = d.pop("connected", UNSET)

        link_from_calendar_event = d.pop("linkFromCalendarEvent", UNSET)

        office_meeting_provider_dto = cls(
            code=code,
            connected=connected,
            link_from_calendar_event=link_from_calendar_event,
        )

        return office_meeting_provider_dto

