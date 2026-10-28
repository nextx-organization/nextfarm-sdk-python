from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeSetVisibilityRequest")



@_attrs_define
class OfficeSetVisibilityRequest:
    

    is_visible: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_visible = self.is_visible


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_visible = d.pop("isVisible", UNSET)

        office_set_visibility_request = cls(
            is_visible=is_visible,
        )

        return office_set_visibility_request

