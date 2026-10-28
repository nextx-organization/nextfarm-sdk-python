from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeLikeAnnouncementRequest")



@_attrs_define
class OfficeLikeAnnouncementRequest:
    

    liked: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        liked = self.liked


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if liked is not UNSET:
            field_dict["liked"] = liked

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        liked = d.pop("liked", UNSET)

        office_like_announcement_request = cls(
            liked=liked,
        )

        return office_like_announcement_request

