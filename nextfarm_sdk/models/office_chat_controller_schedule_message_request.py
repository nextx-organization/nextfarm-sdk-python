from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeChatControllerScheduleMessageRequest")



@_attrs_define
class OfficeChatControllerScheduleMessageRequest:
    

    content: None | str | Unset = UNSET
    scheduled_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        scheduled_at: str | Unset = UNSET
        if not isinstance(self.scheduled_at, Unset):
            scheduled_at = self.scheduled_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if scheduled_at is not UNSET:
            field_dict["scheduledAt"] = scheduled_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        _scheduled_at = d.pop("scheduledAt", UNSET)
        scheduled_at: datetime.datetime | Unset
        if isinstance(_scheduled_at,  Unset):
            scheduled_at = UNSET
        else:
            scheduled_at = datetime.datetime.fromisoformat(_scheduled_at)




        office_chat_controller_schedule_message_request = cls(
            content=content,
            scheduled_at=scheduled_at,
        )

        return office_chat_controller_schedule_message_request

