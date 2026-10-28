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






T = TypeVar("T", bound="OfficeChatControllerCreateChatReminderRequest")



@_attrs_define
class OfficeChatControllerCreateChatReminderRequest:
    

    channel_id: None | Unset | UUID = UNSET
    message_id: None | Unset | UUID = UNSET
    remind_at: datetime.datetime | Unset = UNSET
    text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: None | str | Unset
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        elif isinstance(self.channel_id, UUID):
            channel_id = str(self.channel_id)
        else:
            channel_id = self.channel_id

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        elif isinstance(self.message_id, UUID):
            message_id = str(self.message_id)
        else:
            message_id = self.message_id

        remind_at: str | Unset = UNSET
        if not isinstance(self.remind_at, Unset):
            remind_at = self.remind_at.isoformat()

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if remind_at is not UNSET:
            field_dict["remindAt"] = remind_at
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_channel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                channel_id_type_0 = UUID(data)



                return channel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        channel_id = _parse_channel_id(d.pop("channelId", UNSET))


        def _parse_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                message_id_type_0 = UUID(data)



                return message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        message_id = _parse_message_id(d.pop("messageId", UNSET))


        _remind_at = d.pop("remindAt", UNSET)
        remind_at: datetime.datetime | Unset
        if isinstance(_remind_at,  Unset):
            remind_at = UNSET
        else:
            remind_at = datetime.datetime.fromisoformat(_remind_at)




        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        office_chat_controller_create_chat_reminder_request = cls(
            channel_id=channel_id,
            message_id=message_id,
            remind_at=remind_at,
            text=text,
        )

        return office_chat_controller_create_chat_reminder_request

