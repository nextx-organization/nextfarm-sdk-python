from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChannelInvitePreviewDto")



@_attrs_define
class OfficeChannelInvitePreviewDto:
    

    already_member: bool | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    channel_name: None | str | Unset = UNSET
    channel_type: None | str | Unset = UNSET
    is_usable: bool | Unset = UNSET
    member_count: int | Unset = UNSET
    reason: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        already_member = self.already_member

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        channel_name: None | str | Unset
        if isinstance(self.channel_name, Unset):
            channel_name = UNSET
        else:
            channel_name = self.channel_name

        channel_type: None | str | Unset
        if isinstance(self.channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = self.channel_type

        is_usable = self.is_usable

        member_count = self.member_count

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if already_member is not UNSET:
            field_dict["alreadyMember"] = already_member
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if channel_name is not UNSET:
            field_dict["channelName"] = channel_name
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if is_usable is not UNSET:
            field_dict["isUsable"] = is_usable
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        already_member = d.pop("alreadyMember", UNSET)

        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        def _parse_channel_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_name = _parse_channel_name(d.pop("channelName", UNSET))


        def _parse_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_type = _parse_channel_type(d.pop("channelType", UNSET))


        is_usable = d.pop("isUsable", UNSET)

        member_count = d.pop("memberCount", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        office_channel_invite_preview_dto = cls(
            already_member=already_member,
            channel_id=channel_id,
            channel_name=channel_name,
            channel_type=channel_type,
            is_usable=is_usable,
            member_count=member_count,
            reason=reason,
        )

        return office_channel_invite_preview_dto

