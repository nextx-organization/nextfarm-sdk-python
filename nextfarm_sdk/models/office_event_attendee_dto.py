from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeEventAttendeeDto")



@_attrs_define
class OfficeEventAttendeeDto:
    

    email: None | str | Unset = UNSET
    is_optional: bool | Unset = UNSET
    is_organizer: bool | Unset = UNSET
    response_note: None | str | Unset = UNSET
    response_status: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        is_optional = self.is_optional

        is_organizer = self.is_organizer

        response_note: None | str | Unset
        if isinstance(self.response_note, Unset):
            response_note = UNSET
        else:
            response_note = self.response_note

        response_status: None | str | Unset
        if isinstance(self.response_status, Unset):
            response_status = UNSET
        else:
            response_status = self.response_status

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if is_optional is not UNSET:
            field_dict["isOptional"] = is_optional
        if is_organizer is not UNSET:
            field_dict["isOrganizer"] = is_organizer
        if response_note is not UNSET:
            field_dict["responseNote"] = response_note
        if response_status is not UNSET:
            field_dict["responseStatus"] = response_status
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        is_optional = d.pop("isOptional", UNSET)

        is_organizer = d.pop("isOrganizer", UNSET)

        def _parse_response_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_note = _parse_response_note(d.pop("responseNote", UNSET))


        def _parse_response_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_status = _parse_response_status(d.pop("responseStatus", UNSET))


        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)



                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


        office_event_attendee_dto = cls(
            email=email,
            is_optional=is_optional,
            is_organizer=is_organizer,
            response_note=response_note,
            response_status=response_status,
            user_id=user_id,
        )

        return office_event_attendee_dto

