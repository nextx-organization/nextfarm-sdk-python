from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeInviteAttendeesRequest")



@_attrs_define
class OfficeInviteAttendeesRequest:
    

    guest_emails: list[str] | None | Unset = UNSET
    user_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        guest_emails: list[str] | None | Unset
        if isinstance(self.guest_emails, Unset):
            guest_emails = UNSET
        elif isinstance(self.guest_emails, list):
            guest_emails = self.guest_emails


        else:
            guest_emails = self.guest_emails

        user_ids: list[str] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = []
            for user_ids_type_0_item_data in self.user_ids:
                user_ids_type_0_item = str(user_ids_type_0_item_data)
                user_ids.append(user_ids_type_0_item)


        else:
            user_ids = self.user_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if guest_emails is not UNSET:
            field_dict["guestEmails"] = guest_emails
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_guest_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guest_emails_type_0 = cast(list[str], data)

                return guest_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guest_emails = _parse_guest_emails(d.pop("guestEmails", UNSET))


        def _parse_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = []
                _user_ids_type_0 = data
                for user_ids_type_0_item_data in (_user_ids_type_0):
                    user_ids_type_0_item = UUID(user_ids_type_0_item_data)



                    user_ids_type_0.append(user_ids_type_0_item)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("userIds", UNSET))


        office_invite_attendees_request = cls(
            guest_emails=guest_emails,
            user_ids=user_ids,
        )

        return office_invite_attendees_request

