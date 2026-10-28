from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficePublicContactCardDto")



@_attrs_define
class OfficePublicContactCardDto:
    

    avatar_url: None | str | Unset = UNSET
    is_usable: bool | Unset = UNSET
    organization_name: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        is_usable = self.is_usable

        organization_name: None | str | Unset
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if is_usable is not UNSET:
            field_dict["isUsable"] = is_usable
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name

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


        is_usable = d.pop("isUsable", UNSET)

        def _parse_organization_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))


        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("ownerName", UNSET))


        office_public_contact_card_dto = cls(
            avatar_url=avatar_url,
            is_usable=is_usable,
            organization_name=organization_name,
            owner_name=owner_name,
        )

        return office_public_contact_card_dto

