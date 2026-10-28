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






T = TypeVar("T", bound="OfficeScheduledMessageDto")



@_attrs_define
class OfficeScheduledMessageDto:
    

    channel_id: UUID | Unset = UNSET
    content: None | str | Unset = UNSET
    failure_key: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    scheduled_at: datetime.datetime | Unset = UNSET
    sent_message_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        failure_key: None | str | Unset
        if isinstance(self.failure_key, Unset):
            failure_key = UNSET
        else:
            failure_key = self.failure_key

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        scheduled_at: str | Unset = UNSET
        if not isinstance(self.scheduled_at, Unset):
            scheduled_at = self.scheduled_at.isoformat()

        sent_message_id: None | str | Unset
        if isinstance(self.sent_message_id, Unset):
            sent_message_id = UNSET
        elif isinstance(self.sent_message_id, UUID):
            sent_message_id = str(self.sent_message_id)
        else:
            sent_message_id = self.sent_message_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if content is not UNSET:
            field_dict["content"] = content
        if failure_key is not UNSET:
            field_dict["failureKey"] = failure_key
        if id is not UNSET:
            field_dict["id"] = id
        if scheduled_at is not UNSET:
            field_dict["scheduledAt"] = scheduled_at
        if sent_message_id is not UNSET:
            field_dict["sentMessageId"] = sent_message_id
        if status is not UNSET:
            field_dict["status"] = status

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


        def _parse_failure_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_key = _parse_failure_key(d.pop("failureKey", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _scheduled_at = d.pop("scheduledAt", UNSET)
        scheduled_at: datetime.datetime | Unset
        if isinstance(_scheduled_at,  Unset):
            scheduled_at = UNSET
        else:
            scheduled_at = datetime.datetime.fromisoformat(_scheduled_at)




        def _parse_sent_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_message_id_type_0 = UUID(data)



                return sent_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sent_message_id = _parse_sent_message_id(d.pop("sentMessageId", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_scheduled_message_dto = cls(
            channel_id=channel_id,
            content=content,
            failure_key=failure_key,
            id=id,
            scheduled_at=scheduled_at,
            sent_message_id=sent_message_id,
            status=status,
        )

        return office_scheduled_message_dto

