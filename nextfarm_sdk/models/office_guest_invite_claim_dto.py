from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeGuestInviteClaimDto")



@_attrs_define
class OfficeGuestInviteClaimDto:
    

    already_member: bool | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    channel_name: None | str | Unset = UNSET
    needs_switch: bool | Unset = UNSET
    workspace_id: UUID | Unset = UNSET





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

        needs_switch = self.needs_switch

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if already_member is not UNSET:
            field_dict["alreadyMember"] = already_member
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if channel_name is not UNSET:
            field_dict["channelName"] = channel_name
        if needs_switch is not UNSET:
            field_dict["needsSwitch"] = needs_switch
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

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


        needs_switch = d.pop("needsSwitch", UNSET)

        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        office_guest_invite_claim_dto = cls(
            already_member=already_member,
            channel_id=channel_id,
            channel_name=channel_name,
            needs_switch=needs_switch,
            workspace_id=workspace_id,
        )

        return office_guest_invite_claim_dto

