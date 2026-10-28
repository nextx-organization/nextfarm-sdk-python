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






T = TypeVar("T", bound="OfficeChannelLinkDto")



@_attrs_define
class OfficeChannelLinkDto:
    

    created_at: datetime.datetime | Unset = UNSET
    message_id: UUID | Unset = UNSET
    sender_id: UUID | Unset = UNSET
    title: None | str | Unset = UNSET
    url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        sender_id: str | Unset = UNSET
        if not isinstance(self.sender_id, Unset):
            sender_id = str(self.sender_id)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        _sender_id = d.pop("senderId", UNSET)
        sender_id: UUID | Unset
        if isinstance(_sender_id,  Unset):
            sender_id = UNSET
        else:
            sender_id = UUID(_sender_id)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        office_channel_link_dto = cls(
            created_at=created_at,
            message_id=message_id,
            sender_id=sender_id,
            title=title,
            url=url,
        )

        return office_channel_link_dto

