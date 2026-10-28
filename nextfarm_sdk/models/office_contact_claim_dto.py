from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeContactClaimDto")



@_attrs_define
class OfficeContactClaimDto:
    

    already_member: bool | Unset = UNSET
    channel_id: None | Unset | UUID = UNSET
    needs_switch: bool | Unset = UNSET
    owner_user_id: UUID | Unset = UNSET
    workspace_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        already_member = self.already_member

        channel_id: None | str | Unset
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        elif isinstance(self.channel_id, UUID):
            channel_id = str(self.channel_id)
        else:
            channel_id = self.channel_id

        needs_switch = self.needs_switch

        owner_user_id: str | Unset = UNSET
        if not isinstance(self.owner_user_id, Unset):
            owner_user_id = str(self.owner_user_id)

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
        if needs_switch is not UNSET:
            field_dict["needsSwitch"] = needs_switch
        if owner_user_id is not UNSET:
            field_dict["ownerUserId"] = owner_user_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        already_member = d.pop("alreadyMember", UNSET)

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


        needs_switch = d.pop("needsSwitch", UNSET)

        _owner_user_id = d.pop("ownerUserId", UNSET)
        owner_user_id: UUID | Unset
        if isinstance(_owner_user_id,  Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = UUID(_owner_user_id)




        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        office_contact_claim_dto = cls(
            already_member=already_member,
            channel_id=channel_id,
            needs_switch=needs_switch,
            owner_user_id=owner_user_id,
            workspace_id=workspace_id,
        )

        return office_contact_claim_dto

