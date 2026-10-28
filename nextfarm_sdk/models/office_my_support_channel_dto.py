from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeMySupportChannelDto")



@_attrs_define
class OfficeMySupportChannelDto:
    

    available: bool | Unset = UNSET
    channel_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    unread_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        available = self.available

        channel_id: None | str | Unset
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        elif isinstance(self.channel_id, UUID):
            channel_id = str(self.channel_id)
        else:
            channel_id = self.channel_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        unread_count = self.unread_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if available is not UNSET:
            field_dict["available"] = available
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if name is not UNSET:
            field_dict["name"] = name
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available", UNSET)

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


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        unread_count = d.pop("unreadCount", UNSET)

        office_my_support_channel_dto = cls(
            available=available,
            channel_id=channel_id,
            name=name,
            unread_count=unread_count,
        )

        return office_my_support_channel_dto

