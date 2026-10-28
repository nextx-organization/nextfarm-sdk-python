from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerUpdateChannelSettingsRequest")



@_attrs_define
class OfficeChatControllerUpdateChannelSettingsRequest:
    

    require_join_approval: bool | None | Unset = UNSET
    who_can_add_members: None | str | Unset = UNSET
    who_can_send_messages: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        require_join_approval: bool | None | Unset
        if isinstance(self.require_join_approval, Unset):
            require_join_approval = UNSET
        else:
            require_join_approval = self.require_join_approval

        who_can_add_members: None | str | Unset
        if isinstance(self.who_can_add_members, Unset):
            who_can_add_members = UNSET
        else:
            who_can_add_members = self.who_can_add_members

        who_can_send_messages: None | str | Unset
        if isinstance(self.who_can_send_messages, Unset):
            who_can_send_messages = UNSET
        else:
            who_can_send_messages = self.who_can_send_messages


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if require_join_approval is not UNSET:
            field_dict["requireJoinApproval"] = require_join_approval
        if who_can_add_members is not UNSET:
            field_dict["whoCanAddMembers"] = who_can_add_members
        if who_can_send_messages is not UNSET:
            field_dict["whoCanSendMessages"] = who_can_send_messages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_require_join_approval(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        require_join_approval = _parse_require_join_approval(d.pop("requireJoinApproval", UNSET))


        def _parse_who_can_add_members(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        who_can_add_members = _parse_who_can_add_members(d.pop("whoCanAddMembers", UNSET))


        def _parse_who_can_send_messages(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        who_can_send_messages = _parse_who_can_send_messages(d.pop("whoCanSendMessages", UNSET))


        office_chat_controller_update_channel_settings_request = cls(
            require_join_approval=require_join_approval,
            who_can_add_members=who_can_add_members,
            who_can_send_messages=who_can_send_messages,
        )

        return office_chat_controller_update_channel_settings_request

