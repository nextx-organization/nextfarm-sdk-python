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






T = TypeVar("T", bound="OfficeHuddleDto")



@_attrs_define
class OfficeHuddleDto:
    

    channel_id: UUID | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    id: UUID | Unset = UNSET
    join_url: None | str | Unset = UNSET
    message_id: None | Unset | UUID = UNSET
    provider: None | str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    started_by: UUID | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        join_url: None | str | Unset
        if isinstance(self.join_url, Unset):
            join_url = UNSET
        else:
            join_url = self.join_url

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        elif isinstance(self.message_id, UUID):
            message_id = str(self.message_id)
        else:
            message_id = self.message_id

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        started_by: str | Unset = UNSET
        if not isinstance(self.started_by, Unset):
            started_by = str(self.started_by)

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
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if id is not UNSET:
            field_dict["id"] = id
        if join_url is not UNSET:
            field_dict["joinUrl"] = join_url
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if started_by is not UNSET:
            field_dict["startedBy"] = started_by
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




        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)



                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_join_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        join_url = _parse_join_url(d.pop("joinUrl", UNSET))


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


        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        _started_by = d.pop("startedBy", UNSET)
        started_by: UUID | Unset
        if isinstance(_started_by,  Unset):
            started_by = UNSET
        else:
            started_by = UUID(_started_by)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_huddle_dto = cls(
            channel_id=channel_id,
            ended_at=ended_at,
            id=id,
            join_url=join_url,
            message_id=message_id,
            provider=provider,
            started_at=started_at,
            started_by=started_by,
            status=status,
        )

        return office_huddle_dto

