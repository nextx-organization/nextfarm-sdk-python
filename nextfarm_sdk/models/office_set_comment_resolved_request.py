from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeSetCommentResolvedRequest")



@_attrs_define
class OfficeSetCommentResolvedRequest:
    

    resolved: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        resolved = self.resolved


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if resolved is not UNSET:
            field_dict["resolved"] = resolved

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resolved = d.pop("resolved", UNSET)

        office_set_comment_resolved_request = cls(
            resolved=resolved,
        )

        return office_set_comment_resolved_request

