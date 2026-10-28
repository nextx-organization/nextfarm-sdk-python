from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeCompleteTaskWithMessagePhotosResponse")



@_attrs_define
class OfficeCompleteTaskWithMessagePhotosResponse:
    

    photos_attached: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        photos_attached = self.photos_attached


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if photos_attached is not UNSET:
            field_dict["photosAttached"] = photos_attached

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photos_attached = d.pop("photosAttached", UNSET)

        office_complete_task_with_message_photos_response = cls(
            photos_attached=photos_attached,
        )

        return office_complete_task_with_message_photos_response

