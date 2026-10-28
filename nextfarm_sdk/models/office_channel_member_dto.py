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






T = TypeVar("T", bound="OfficeChannelMemberDto")



@_attrs_define
class OfficeChannelMemberDto:
    

    is_guest: bool | Unset = UNSET
    joined_at: datetime.datetime | Unset = UNSET
    last_read_at: datetime.datetime | None | Unset = UNSET
    member_name: None | str | Unset = UNSET
    member_org_id: None | Unset | UUID = UNSET
    muted_until: datetime.datetime | None | Unset = UNSET
    notification_level: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        member_name: None | str | Unset
        if isinstance(self.member_name, Unset):
            member_name = UNSET
        else:
            member_name = self.member_name

        member_org_id: None | str | Unset
        if isinstance(self.member_org_id, Unset):
            member_org_id = UNSET
        elif isinstance(self.member_org_id, UUID):
            member_org_id = str(self.member_org_id)
        else:
            member_org_id = self.member_org_id

        muted_until: None | str | Unset
        if isinstance(self.muted_until, Unset):
            muted_until = UNSET
        elif isinstance(self.muted_until, datetime.datetime):
            muted_until = self.muted_until.isoformat()
        else:
            muted_until = self.muted_until

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
        if is_guest is not UNSET:
            field_dict["isGuest"] = is_guest
        if joined_at is not UNSET:
            field_dict["joinedAt"] = joined_at
        if last_read_at is not UNSET:
            field_dict["lastReadAt"] = last_read_at
        if member_name is not UNSET:
            field_dict["memberName"] = member_name
        if member_org_id is not UNSET:
            field_dict["memberOrgId"] = member_org_id
        if muted_until is not UNSET:
            field_dict["mutedUntil"] = muted_until
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


        def _parse_member_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_name = _parse_member_name(d.pop("memberName", UNSET))


        def _parse_member_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                member_org_id_type_0 = UUID(data)



                return member_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        member_org_id = _parse_member_org_id(d.pop("memberOrgId", UNSET))


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




        office_channel_member_dto = cls(
            is_guest=is_guest,
            joined_at=joined_at,
            last_read_at=last_read_at,
            member_name=member_name,
            member_org_id=member_org_id,
            muted_until=muted_until,
            notification_level=notification_level,
            role=role,
            user_id=user_id,
        )

        return office_channel_member_dto

