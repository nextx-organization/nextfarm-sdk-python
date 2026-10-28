from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeCreateMomentRequest")



@_attrs_define
class OfficeCreateMomentRequest:
    

    caption: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if caption is not UNSET:
            field_dict["caption"] = caption

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))


        office_create_moment_request = cls(
            caption=caption,
        )

        return office_create_moment_request

