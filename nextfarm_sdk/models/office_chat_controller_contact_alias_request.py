from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerContactAliasRequest")



@_attrs_define
class OfficeChatControllerContactAliasRequest:
    

    alias: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        office_chat_controller_contact_alias_request = cls(
            alias=alias,
        )

        return office_chat_controller_contact_alias_request

