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






T = TypeVar("T", bound="OfficeChatSearchFileDto")



@_attrs_define
class OfficeChatSearchFileDto:
    

    attachment_id: UUID | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    content_type: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    file_name: None | str | Unset = UNSET
    message_id: UUID | Unset = UNSET
    size_bytes: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        attachment_id: str | Unset = UNSET
        if not isinstance(self.attachment_id, Unset):
            attachment_id = str(self.attachment_id)

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        size_bytes = self.size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _attachment_id = d.pop("attachmentId", UNSET)
        attachment_id: UUID | Unset
        if isinstance(_attachment_id,  Unset):
            attachment_id = UNSET
        else:
            attachment_id = UUID(_attachment_id)




        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        size_bytes = d.pop("sizeBytes", UNSET)

        office_chat_search_file_dto = cls(
            attachment_id=attachment_id,
            channel_id=channel_id,
            content_type=content_type,
            created_at=created_at,
            file_name=file_name,
            message_id=message_id,
            size_bytes=size_bytes,
        )

        return office_chat_search_file_dto

