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






T = TypeVar("T", bound="OfficeChannelMemberListItemDto")



@_attrs_define
class OfficeChannelMemberListItemDto:
    

    display_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    is_guest: bool | Unset = UNSET
    joined_at: datetime.datetime | Unset = UNSET
    last_read_at: datetime.datetime | None | Unset = UNSET
    notification_level: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        is_guest = self.is_guest

        joined_at: str | Unset = UNSET
        if not isinstance(self.joined_at, Unset):
            joined_at = self.joined_at.isoformat()

        last_read_at: None | str | Unset
        if isinstance(self.last_read_at, Unset):
            last_read_at = UNSET
        elif isinstance(self.last_read_at, datetime.datetime):
            last_read_at = self.last_read_at.isoformat()
        else:
            last_read_at = self.last_read_at

        notification_level: None | str | Unset
        if isinstance(self.notification_level, Unset):
            notification_level = UNSET
        else:
            notification_level = self.notification_level

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_guest is not UNSET:
            field_dict["isGuest"] = is_guest
        if joined_at is not UNSET:
            field_dict["joinedAt"] = joined_at
        if last_read_at is not UNSET:
            field_dict["lastReadAt"] = last_read_at
        if notification_level is not UNSET:
            field_dict["notificationLevel"] = notification_level
        if role is not UNSET:
            field_dict["role"] = role
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        is_guest = d.pop("isGuest", UNSET)

        _joined_at = d.pop("joinedAt", UNSET)
        joined_at: datetime.datetime | Unset
        if isinstance(_joined_at,  Unset):
            joined_at = UNSET
        else:
            joined_at = datetime.datetime.fromisoformat(_joined_at)




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


        def _parse_notification_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_level = _parse_notification_level(d.pop("notificationLevel", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_channel_member_list_item_dto = cls(
            display_name=display_name,
            email=email,
            is_guest=is_guest,
            joined_at=joined_at,
            last_read_at=last_read_at,
            notification_level=notification_level,
            role=role,
            user_id=user_id,
        )

        return office_channel_member_list_item_dto

