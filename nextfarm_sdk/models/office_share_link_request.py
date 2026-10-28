from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeShareLinkRequest")



@_attrs_define
class OfficeShareLinkRequest:
    

    external_recipient: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        external_recipient = self.external_recipient


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if external_recipient is not UNSET:
            field_dict["externalRecipient"] = external_recipient

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_recipient = d.pop("externalRecipient", UNSET)

        office_share_link_request = cls(
            external_recipient=external_recipient,
        )

        return office_share_link_request

