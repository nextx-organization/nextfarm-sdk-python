from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficePublicContactClaimDto")



@_attrs_define
class OfficePublicContactClaimDto:
    

    email_sent_to: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        email_sent_to: None | str | Unset
        if isinstance(self.email_sent_to, Unset):
            email_sent_to = UNSET
        else:
            email_sent_to = self.email_sent_to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if email_sent_to is not UNSET:
            field_dict["emailSentTo"] = email_sent_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_email_sent_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_sent_to = _parse_email_sent_to(d.pop("emailSentTo", UNSET))


        office_public_contact_claim_dto = cls(
            email_sent_to=email_sent_to,
        )

        return office_public_contact_claim_dto

