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






T = TypeVar("T", bound="OfficeChatJoinRequestDto")



@_attrs_define
class OfficeChatJoinRequestDto:
    

    channel_id: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    decided_at: datetime.datetime | None | Unset = UNSET
    decided_by: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    invited_by: None | Unset | UUID = UNSET
    is_guest: bool | Unset = UNSET
    source: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        decided_at: None | str | Unset
        if isinstance(self.decided_at, Unset):
            decided_at = UNSET
        elif isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        decided_by: None | str | Unset
        if isinstance(self.decided_by, Unset):
            decided_by = UNSET
        elif isinstance(self.decided_by, UUID):
            decided_by = str(self.decided_by)
        else:
            decided_by = self.decided_by

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        invited_by: None | str | Unset
        if isinstance(self.invited_by, Unset):
            invited_by = UNSET
        elif isinstance(self.invited_by, UUID):
            invited_by = str(self.invited_by)
        else:
            invited_by = self.invited_by

        is_guest = self.is_guest

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if decided_at is not UNSET:
            field_dict["decidedAt"] = decided_at
        if decided_by is not UNSET:
            field_dict["decidedBy"] = decided_by
        if id is not UNSET:
            field_dict["id"] = id
        if invited_by is not UNSET:
            field_dict["invitedBy"] = invited_by
        if is_guest is not UNSET:
            field_dict["isGuest"] = is_guest
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id,  Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_decided_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_at_type_0 = datetime.datetime.fromisoformat(data)



                return decided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        decided_at = _parse_decided_at(d.pop("decidedAt", UNSET))


        def _parse_decided_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_by_type_0 = UUID(data)



                return decided_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        decided_by = _parse_decided_by(d.pop("decidedBy", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_invited_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invited_by_type_0 = UUID(data)



                return invited_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        invited_by = _parse_invited_by(d.pop("invitedBy", UNSET))


        is_guest = d.pop("isGuest", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_chat_join_request_dto = cls(
            channel_id=channel_id,
            created_at=created_at,
            decided_at=decided_at,
            decided_by=decided_by,
            id=id,
            invited_by=invited_by,
            is_guest=is_guest,
            source=source,
            status=status,
            user_id=user_id,
        )

        return office_chat_join_request_dto

