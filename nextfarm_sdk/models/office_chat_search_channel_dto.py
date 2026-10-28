from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatSearchChannelDto")



@_attrs_define
class OfficeChatSearchChannelDto:
    

    channel_id: UUID | Unset = UNSET
    channel_type: None | str | Unset = UNSET
    matching_messages: int | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        channel_type: None | str | Unset
        if isinstance(self.channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = self.channel_type

        matching_messages = self.matching_messages

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if matching_messages is not UNSET:
            field_dict["matchingMessages"] = matching_messages
        if name is not UNSET:
            field_dict["name"] = name

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




        def _parse_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_type = _parse_channel_type(d.pop("channelType", UNSET))


        matching_messages = d.pop("matchingMessages", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_chat_search_channel_dto = cls(
            channel_id=channel_id,
            channel_type=channel_type,
            matching_messages=matching_messages,
            name=name,
        )

        return office_chat_search_channel_dto

