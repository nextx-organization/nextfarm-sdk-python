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






T = TypeVar("T", bound="OfficeChannelListItemDto")



@_attrs_define
class OfficeChannelListItemDto:
    

    avatar_url: None | str | Unset = UNSET
    category_id: None | Unset | UUID = UNSET
    channel_type: None | str | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_archived_for_me: bool | Unset = UNSET
    is_frozen: bool | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    is_pinned: bool | Unset = UNSET
    is_shared: bool | Unset = UNSET
    label_ids: list[UUID] | None | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    last_message_preview: None | str | Unset = UNSET
    last_message_sender_id: None | Unset | UUID = UNSET
    last_message_state: None | str | Unset = UNSET
    last_read_at: datetime.datetime | None | Unset = UNSET
    member_count: int | None | Unset = UNSET
    member_user_ids: list[UUID] | None | Unset = UNSET
    muted_until: datetime.datetime | None | Unset = UNSET
    my_role: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    notification_level: None | str | Unset = UNSET
    peer_user_id: None | Unset | UUID = UNSET
    role: None | str | Unset = UNSET
    unread_count: int | Unset = UNSET
    unread_mention_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        elif isinstance(self.category_id, UUID):
            category_id = str(self.category_id)
        else:
            category_id = self.category_id

        channel_type: None | str | Unset
        if isinstance(self.channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = self.channel_type

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_archived = self.is_archived

        is_archived_for_me = self.is_archived_for_me

        is_frozen = self.is_frozen

        is_hidden = self.is_hidden

        is_pinned = self.is_pinned

        is_shared = self.is_shared

        label_ids: list[str] | None | Unset
        if isinstance(self.label_ids, Unset):
            label_ids = UNSET
        elif isinstance(self.label_ids, list):
            label_ids = []
            for label_ids_type_0_item_data in self.label_ids:
                label_ids_type_0_item = str(label_ids_type_0_item_data)
                label_ids.append(label_ids_type_0_item)


        else:
            label_ids = self.label_ids

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        last_message_preview: None | str | Unset
        if isinstance(self.last_message_preview, Unset):
            last_message_preview = UNSET
        else:
            last_message_preview = self.last_message_preview

        last_message_sender_id: None | str | Unset
        if isinstance(self.last_message_sender_id, Unset):
            last_message_sender_id = UNSET
        elif isinstance(self.last_message_sender_id, UUID):
            last_message_sender_id = str(self.last_message_sender_id)
        else:
            last_message_sender_id = self.last_message_sender_id

        last_message_state: None | str | Unset
        if isinstance(self.last_message_state, Unset):
            last_message_state = UNSET
        else:
            last_message_state = self.last_message_state

        last_read_at: None | str | Unset
        if isinstance(self.last_read_at, Unset):
            last_read_at = UNSET
        elif isinstance(self.last_read_at, datetime.datetime):
            last_read_at = self.last_read_at.isoformat()
        else:
            last_read_at = self.last_read_at

        member_count: int | None | Unset
        if isinstance(self.member_count, Unset):
            member_count = UNSET
        else:
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

        muted_until: None | str | Unset
        if isinstance(self.muted_until, Unset):
            muted_until = UNSET
        elif isinstance(self.muted_until, datetime.datetime):
            muted_until = self.muted_until.isoformat()
        else:
            muted_until = self.muted_until

        my_role: None | str | Unset
        if isinstance(self.my_role, Unset):
            my_role = UNSET
        else:
            my_role = self.my_role

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        notification_level: None | str | Unset
        if isinstance(self.notification_level, Unset):
            notification_level = UNSET
        else:
            notification_level = self.notification_level

        peer_user_id: None | str | Unset
        if isinstance(self.peer_user_id, Unset):
            peer_user_id = UNSET
        elif isinstance(self.peer_user_id, UUID):
            peer_user_id = str(self.peer_user_id)
        else:
            peer_user_id = self.peer_user_id

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        unread_count = self.unread_count

        unread_mention_count = self.unread_mention_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_archived_for_me is not UNSET:
            field_dict["isArchivedForMe"] = is_archived_for_me
        if is_frozen is not UNSET:
            field_dict["isFrozen"] = is_frozen
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if is_shared is not UNSET:
            field_dict["isShared"] = is_shared
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if last_message_preview is not UNSET:
            field_dict["lastMessagePreview"] = last_message_preview
        if last_message_sender_id is not UNSET:
            field_dict["lastMessageSenderId"] = last_message_sender_id
        if last_message_state is not UNSET:
            field_dict["lastMessageState"] = last_message_state
        if last_read_at is not UNSET:
            field_dict["lastReadAt"] = last_read_at
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if member_user_ids is not UNSET:
            field_dict["memberUserIds"] = member_user_ids
        if muted_until is not UNSET:
            field_dict["mutedUntil"] = muted_until
        if my_role is not UNSET:
            field_dict["myRole"] = my_role
        if name is not UNSET:
            field_dict["name"] = name
        if notification_level is not UNSET:
            field_dict["notificationLevel"] = notification_level
        if peer_user_id is not UNSET:
            field_dict["peerUserId"] = peer_user_id
        if role is not UNSET:
            field_dict["role"] = role
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count
        if unread_mention_count is not UNSET:
            field_dict["unreadMentionCount"] = unread_mention_count

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


        def _parse_category_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_id_type_0 = UUID(data)



                return category_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))


        def _parse_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_type = _parse_channel_type(d.pop("channelType", UNSET))


        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)



                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_archived = d.pop("isArchived", UNSET)

        is_archived_for_me = d.pop("isArchivedForMe", UNSET)

        is_frozen = d.pop("isFrozen", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        is_pinned = d.pop("isPinned", UNSET)

        is_shared = d.pop("isShared", UNSET)

        def _parse_label_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                label_ids_type_0 = []
                _label_ids_type_0 = data
                for label_ids_type_0_item_data in (_label_ids_type_0):
                    label_ids_type_0_item = UUID(label_ids_type_0_item_data)



                    label_ids_type_0.append(label_ids_type_0_item)

                return label_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        label_ids = _parse_label_ids(d.pop("labelIds", UNSET))


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


        def _parse_last_message_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_message_preview = _parse_last_message_preview(d.pop("lastMessagePreview", UNSET))


        def _parse_last_message_sender_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_sender_id_type_0 = UUID(data)



                return last_message_sender_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        last_message_sender_id = _parse_last_message_sender_id(d.pop("lastMessageSenderId", UNSET))


        def _parse_last_message_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_message_state = _parse_last_message_state(d.pop("lastMessageState", UNSET))


        def _parse_last_read_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_read_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_read_at = _parse_last_read_at(d.pop("lastReadAt", UNSET))


        def _parse_member_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        member_count = _parse_member_count(d.pop("memberCount", UNSET))


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


        def _parse_muted_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                muted_until_type_0 = datetime.datetime.fromisoformat(data)



                return muted_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        muted_until = _parse_muted_until(d.pop("mutedUntil", UNSET))


        def _parse_my_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        my_role = _parse_my_role(d.pop("myRole", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_notification_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_level = _parse_notification_level(d.pop("notificationLevel", UNSET))


        def _parse_peer_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                peer_user_id_type_0 = UUID(data)



                return peer_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        peer_user_id = _parse_peer_user_id(d.pop("peerUserId", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        unread_count = d.pop("unreadCount", UNSET)

        unread_mention_count = d.pop("unreadMentionCount", UNSET)

        office_channel_list_item_dto = cls(
            avatar_url=avatar_url,
            category_id=category_id,
            channel_type=channel_type,
            created_by=created_by,
            description=description,
            id=id,
            is_archived=is_archived,
            is_archived_for_me=is_archived_for_me,
            is_frozen=is_frozen,
            is_hidden=is_hidden,
            is_pinned=is_pinned,
            is_shared=is_shared,
            label_ids=label_ids,
            last_message_at=last_message_at,
            last_message_preview=last_message_preview,
            last_message_sender_id=last_message_sender_id,
            last_message_state=last_message_state,
            last_read_at=last_read_at,
            member_count=member_count,
            member_user_ids=member_user_ids,
            muted_until=muted_until,
            my_role=my_role,
            name=name,
            notification_level=notification_level,
            peer_user_id=peer_user_id,
            role=role,
            unread_count=unread_count,
            unread_mention_count=unread_mention_count,
        )

        return office_channel_list_item_dto

