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






T = TypeVar("T", bound="OfficeChatDraftDto")



@_attrs_define
class OfficeChatDraftDto:
    

    channel_id: UUID | Unset = UNSET
    content: None | str | Unset = UNSET
    quoted_message_id: None | Unset | UUID = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        quoted_message_id: None | str | Unset
        if isinstance(self.quoted_message_id, Unset):
            quoted_message_id = UNSET
        elif isinstance(self.quoted_message_id, UUID):
            quoted_message_id = str(self.quoted_message_id)
        else:
            quoted_message_id = self.quoted_message_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if content is not UNSET:
            field_dict["content"] = content
        if quoted_message_id is not UNSET:
            field_dict["quotedMessageId"] = quoted_message_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_quoted_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quoted_message_id_type_0 = UUID(data)



                return quoted_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        quoted_message_id = _parse_quoted_message_id(d.pop("quotedMessageId", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_chat_draft_dto = cls(
            channel_id=channel_id,
            content=content,
            quoted_message_id=quoted_message_id,
            updated_at=updated_at,
        )

        return office_chat_draft_dto

