from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatSearchContactDto")



@_attrs_define
class OfficeChatSearchContactDto:
    

    direct_channel_id: None | Unset | UUID = UNSET
    email: None | str | Unset = UNSET
    matched_by: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        direct_channel_id: None | str | Unset
        if isinstance(self.direct_channel_id, Unset):
            direct_channel_id = UNSET
        elif isinstance(self.direct_channel_id, UUID):
            direct_channel_id = str(self.direct_channel_id)
        else:
            direct_channel_id = self.direct_channel_id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        matched_by: None | str | Unset
        if isinstance(self.matched_by, Unset):
            matched_by = UNSET
        else:
            matched_by = self.matched_by

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if direct_channel_id is not UNSET:
            field_dict["directChannelId"] = direct_channel_id
        if email is not UNSET:
            field_dict["email"] = email
        if matched_by is not UNSET:
            field_dict["matchedBy"] = matched_by
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_direct_channel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                direct_channel_id_type_0 = UUID(data)



                return direct_channel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        direct_channel_id = _parse_direct_channel_id(d.pop("directChannelId", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_matched_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        matched_by = _parse_matched_by(d.pop("matchedBy", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_chat_search_contact_dto = cls(
            direct_channel_id=direct_channel_id,
            email=email,
            matched_by=matched_by,
            name=name,
            phone=phone,
            user_id=user_id,
        )

        return office_chat_search_contact_dto

