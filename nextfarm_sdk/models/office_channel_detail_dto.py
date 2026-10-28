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

if TYPE_CHECKING:
  from ..models.office_channel_member_dto import OfficeChannelMemberDto
  from ..models.office_channel_my_settings_dto import OfficeChannelMySettingsDto





T = TypeVar("T", bound="OfficeChannelDetailDto")



@_attrs_define
class OfficeChannelDetailDto:
    

    allow_guests: bool | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    can_add_members: bool | Unset = UNSET
    can_send_messages: bool | Unset = UNSET
    channel_type: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    frozen_at: datetime.datetime | None | Unset = UNSET
    frozen_by: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_frozen: bool | Unset = UNSET
    is_shared: bool | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    meeting_url: None | str | Unset = UNSET
    members: list[OfficeChannelMemberDto] | None | Unset = UNSET
    my_label_ids: list[UUID] | None | Unset = UNSET
    my_role: None | str | Unset = UNSET
    my_settings: OfficeChannelMySettingsDto | Unset = UNSET
    name: None | str | Unset = UNSET
    peer_left: bool | Unset = UNSET
    peer_member_count: int | Unset = UNSET
    peer_org_id: None | Unset | UUID = UNSET
    require_join_approval: bool | Unset = UNSET
    who_can_add_members: None | str | Unset = UNSET
    who_can_send_messages: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_channel_member_dto import OfficeChannelMemberDto # noqa: PLC0415
        from ..models.office_channel_my_settings_dto import OfficeChannelMySettingsDto # noqa: PLC0415
        allow_guests = self.allow_guests

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        can_add_members = self.can_add_members

        can_send_messages = self.can_send_messages

        channel_type: None | str | Unset
        if isinstance(self.channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = self.channel_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        frozen_at: None | str | Unset
        if isinstance(self.frozen_at, Unset):
            frozen_at = UNSET
        elif isinstance(self.frozen_at, datetime.datetime):
            frozen_at = self.frozen_at.isoformat()
        else:
            frozen_at = self.frozen_at

        frozen_by: None | str | Unset
        if isinstance(self.frozen_by, Unset):
            frozen_by = UNSET
        elif isinstance(self.frozen_by, UUID):
            frozen_by = str(self.frozen_by)
        else:
            frozen_by = self.frozen_by

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_archived = self.is_archived

        is_frozen = self.is_frozen

        is_shared = self.is_shared

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        meeting_url: None | str | Unset
        if isinstance(self.meeting_url, Unset):
            meeting_url = UNSET
        else:
            meeting_url = self.meeting_url

        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)


        else:
            members = self.members

        my_label_ids: list[str] | None | Unset
        if isinstance(self.my_label_ids, Unset):
            my_label_ids = UNSET
        elif isinstance(self.my_label_ids, list):
            my_label_ids = []
            for my_label_ids_type_0_item_data in self.my_label_ids:
                my_label_ids_type_0_item = str(my_label_ids_type_0_item_data)
                my_label_ids.append(my_label_ids_type_0_item)


        else:
            my_label_ids = self.my_label_ids

        my_role: None | str | Unset
        if isinstance(self.my_role, Unset):
            my_role = UNSET
        else:
            my_role = self.my_role

        my_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.my_settings, Unset):
            my_settings = self.my_settings.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        peer_left = self.peer_left

        peer_member_count = self.peer_member_count

        peer_org_id: None | str | Unset
        if isinstance(self.peer_org_id, Unset):
            peer_org_id = UNSET
        elif isinstance(self.peer_org_id, UUID):
            peer_org_id = str(self.peer_org_id)
        else:
            peer_org_id = self.peer_org_id

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
        if allow_guests is not UNSET:
            field_dict["allowGuests"] = allow_guests
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if can_add_members is not UNSET:
            field_dict["canAddMembers"] = can_add_members
        if can_send_messages is not UNSET:
            field_dict["canSendMessages"] = can_send_messages
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if description is not UNSET:
            field_dict["description"] = description
        if frozen_at is not UNSET:
            field_dict["frozenAt"] = frozen_at
        if frozen_by is not UNSET:
            field_dict["frozenBy"] = frozen_by
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_frozen is not UNSET:
            field_dict["isFrozen"] = is_frozen
        if is_shared is not UNSET:
            field_dict["isShared"] = is_shared
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if meeting_url is not UNSET:
            field_dict["meetingUrl"] = meeting_url
        if members is not UNSET:
            field_dict["members"] = members
        if my_label_ids is not UNSET:
            field_dict["myLabelIds"] = my_label_ids
        if my_role is not UNSET:
            field_dict["myRole"] = my_role
        if my_settings is not UNSET:
            field_dict["mySettings"] = my_settings
        if name is not UNSET:
            field_dict["name"] = name
        if peer_left is not UNSET:
            field_dict["peerLeft"] = peer_left
        if peer_member_count is not UNSET:
            field_dict["peerMemberCount"] = peer_member_count
        if peer_org_id is not UNSET:
            field_dict["peerOrgId"] = peer_org_id
        if require_join_approval is not UNSET:
            field_dict["requireJoinApproval"] = require_join_approval
        if who_can_add_members is not UNSET:
            field_dict["whoCanAddMembers"] = who_can_add_members
        if who_can_send_messages is not UNSET:
            field_dict["whoCanSendMessages"] = who_can_send_messages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_channel_member_dto import OfficeChannelMemberDto # noqa: PLC0415
        from ..models.office_channel_my_settings_dto import OfficeChannelMySettingsDto # noqa: PLC0415
        d = dict(src_dict)
        allow_guests = d.pop("allowGuests", UNSET)

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        can_add_members = d.pop("canAddMembers", UNSET)

        can_send_messages = d.pop("canSendMessages", UNSET)

        def _parse_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_type = _parse_channel_type(d.pop("channelType", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_frozen_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                frozen_at_type_0 = datetime.datetime.fromisoformat(data)



                return frozen_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        frozen_at = _parse_frozen_at(d.pop("frozenAt", UNSET))


        def _parse_frozen_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                frozen_by_type_0 = UUID(data)



                return frozen_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        frozen_by = _parse_frozen_by(d.pop("frozenBy", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_archived = d.pop("isArchived", UNSET)

        is_frozen = d.pop("isFrozen", UNSET)

        is_shared = d.pop("isShared", UNSET)

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


        def _parse_meeting_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        meeting_url = _parse_meeting_url(d.pop("meetingUrl", UNSET))


        def _parse_members(data: object) -> list[OfficeChannelMemberDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in (_members_type_0):
                    members_type_0_item = OfficeChannelMemberDto.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChannelMemberDto] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


        def _parse_my_label_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                my_label_ids_type_0 = []
                _my_label_ids_type_0 = data
                for my_label_ids_type_0_item_data in (_my_label_ids_type_0):
                    my_label_ids_type_0_item = UUID(my_label_ids_type_0_item_data)



                    my_label_ids_type_0.append(my_label_ids_type_0_item)

                return my_label_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        my_label_ids = _parse_my_label_ids(d.pop("myLabelIds", UNSET))


        def _parse_my_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        my_role = _parse_my_role(d.pop("myRole", UNSET))


        _my_settings = d.pop("mySettings", UNSET)
        my_settings: OfficeChannelMySettingsDto | Unset
        if isinstance(_my_settings,  Unset):
            my_settings = UNSET
        else:
            my_settings = OfficeChannelMySettingsDto.from_dict(_my_settings)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        peer_left = d.pop("peerLeft", UNSET)

        peer_member_count = d.pop("peerMemberCount", UNSET)

        def _parse_peer_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                peer_org_id_type_0 = UUID(data)



                return peer_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        peer_org_id = _parse_peer_org_id(d.pop("peerOrgId", UNSET))


        require_join_approval = d.pop("requireJoinApproval", UNSET)

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


        office_channel_detail_dto = cls(
            allow_guests=allow_guests,
            avatar_url=avatar_url,
            can_add_members=can_add_members,
            can_send_messages=can_send_messages,
            channel_type=channel_type,
            description=description,
            frozen_at=frozen_at,
            frozen_by=frozen_by,
            id=id,
            is_archived=is_archived,
            is_frozen=is_frozen,
            is_shared=is_shared,
            last_message_at=last_message_at,
            meeting_url=meeting_url,
            members=members,
            my_label_ids=my_label_ids,
            my_role=my_role,
            my_settings=my_settings,
            name=name,
            peer_left=peer_left,
            peer_member_count=peer_member_count,
            peer_org_id=peer_org_id,
            require_join_approval=require_join_approval,
            who_can_add_members=who_can_add_members,
            who_can_send_messages=who_can_send_messages,
        )

        return office_channel_detail_dto

