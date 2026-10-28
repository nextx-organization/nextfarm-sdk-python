from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficePublicContactCardsControllerClaimRequest")



@_attrs_define
class OfficePublicContactCardsControllerClaimRequest:
    

    email: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if full_name is not UNSET:
            field_dict["fullName"] = full_name

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


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        office_public_contact_cards_controller_claim_request = cls(
            email=email,
            full_name=full_name,
        )

        return office_public_contact_cards_controller_claim_request

