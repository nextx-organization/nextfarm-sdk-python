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






T = TypeVar("T", bound="OfficeUserSessionDto")



@_attrs_define
class OfficeUserSessionDto:
    

    device_label: None | str | Unset = UNSET
    first_seen_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    is_current: bool | Unset = UNSET
    is_revoked: bool | Unset = UNSET
    last_seen_at: datetime.datetime | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        device_label: None | str | Unset
        if isinstance(self.device_label, Unset):
            device_label = UNSET
        else:
            device_label = self.device_label

        first_seen_at: str | Unset = UNSET
        if not isinstance(self.first_seen_at, Unset):
            first_seen_at = self.first_seen_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        is_current = self.is_current

        is_revoked = self.is_revoked

        last_seen_at: str | Unset = UNSET
        if not isinstance(self.last_seen_at, Unset):
            last_seen_at = self.last_seen_at.isoformat()

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if device_label is not UNSET:
            field_dict["deviceLabel"] = device_label
        if first_seen_at is not UNSET:
            field_dict["firstSeenAt"] = first_seen_at
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if is_revoked is not UNSET:
            field_dict["isRevoked"] = is_revoked
        if last_seen_at is not UNSET:
            field_dict["lastSeenAt"] = last_seen_at
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_device_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_label = _parse_device_label(d.pop("deviceLabel", UNSET))


        _first_seen_at = d.pop("firstSeenAt", UNSET)
        first_seen_at: datetime.datetime | Unset
        if isinstance(_first_seen_at,  Unset):
            first_seen_at = UNSET
        else:
            first_seen_at = datetime.datetime.fromisoformat(_first_seen_at)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))


        is_current = d.pop("isCurrent", UNSET)

        is_revoked = d.pop("isRevoked", UNSET)

        _last_seen_at = d.pop("lastSeenAt", UNSET)
        last_seen_at: datetime.datetime | Unset
        if isinstance(_last_seen_at,  Unset):
            last_seen_at = UNSET
        else:
            last_seen_at = datetime.datetime.fromisoformat(_last_seen_at)




        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_user_session_dto = cls(
            device_label=device_label,
            first_seen_at=first_seen_at,
            id=id,
            ip_address=ip_address,
            is_current=is_current,
            is_revoked=is_revoked,
            last_seen_at=last_seen_at,
            user_id=user_id,
        )

        return office_user_session_dto

