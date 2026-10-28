from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeEventReminderDto")



@_attrs_define
class OfficeEventReminderDto:
    

    channel: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    minutes_before: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        minutes_before = self.minutes_before


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if id is not UNSET:
            field_dict["id"] = id
        if minutes_before is not UNSET:
            field_dict["minutesBefore"] = minutes_before

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        minutes_before = d.pop("minutesBefore", UNSET)

        office_event_reminder_dto = cls(
            channel=channel,
            id=id,
            minutes_before=minutes_before,
        )

        return office_event_reminder_dto

