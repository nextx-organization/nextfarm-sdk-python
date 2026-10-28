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






T = TypeVar("T", bound="OfficeCommonChannelDto")



@_attrs_define
class OfficeCommonChannelDto:
    

    avatar_url: None | str | Unset = UNSET
    channel_type: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    member_count: int | Unset = UNSET
    member_user_ids: list[UUID] | None | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        channel_type: None | str | Unset
        if isinstance(self.channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = self.channel_type

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        member_count = self.member_count

        member_user_ids: list[str] | None | Unset
        if isinstance(self.member_user_ids, Unset):
            member_user_ids = UNSET
        elif isinstance(self.member_user_ids, list):
            member_user_ids = []
            for member_user_ids_type_0_item_data in self.member_user_ids:
                member_user_ids_type_0_item = str(member_user_ids_type_0_item_data)
                member_user_ids.append(member_user_ids_type_0_item)


        else:
            member_user_ids = self.member_user_ids

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if id is not UNSET:
            field_dict["id"] = id
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if member_user_ids is not UNSET:
            field_dict["memberUserIds"] = member_user_ids
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_type = _parse_channel_type(d.pop("channelType", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("lastMessageAt", UNSET))


        member_count = d.pop("memberCount", UNSET)

        def _parse_member_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_user_ids_type_0 = []
                _member_user_ids_type_0 = data
                for member_user_ids_type_0_item_data in (_member_user_ids_type_0):
                    member_user_ids_type_0_item = UUID(member_user_ids_type_0_item_data)



                    member_user_ids_type_0.append(member_user_ids_type_0_item)

                return member_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        member_user_ids = _parse_member_user_ids(d.pop("memberUserIds", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_common_channel_dto = cls(
            avatar_url=avatar_url,
            channel_type=channel_type,
            id=id,
            last_message_at=last_message_at,
            member_count=member_count,
            member_user_ids=member_user_ids,
            name=name,
        )

        return office_common_channel_dto

