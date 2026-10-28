from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeSetDocNodeRestrictedRequest")



@_attrs_define
class OfficeSetDocNodeRestrictedRequest:
    

    restricted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        restricted = self.restricted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if restricted is not UNSET:
            field_dict["restricted"] = restricted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restricted = d.pop("restricted", UNSET)

        office_set_doc_node_restricted_request = cls(
            restricted=restricted,
        )

        return office_set_doc_node_restricted_request

