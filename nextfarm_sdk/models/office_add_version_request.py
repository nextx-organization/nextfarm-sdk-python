from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAddVersionRequest")



@_attrs_define
class OfficeAddVersionRequest:
    

    change_note: None | str | Unset = UNSET
    content_type: None | str | Unset = UNSET
    object_key: None | str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    thumbnail_path: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        change_note: None | str | Unset
        if isinstance(self.change_note, Unset):
            change_note = UNSET
        else:
            change_note = self.change_note

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        object_key: None | str | Unset
        if isinstance(self.object_key, Unset):
            object_key = UNSET
        else:
            object_key = self.object_key

        size_bytes = self.size_bytes

        thumbnail_path: None | str | Unset
        if isinstance(self.thumbnail_path, Unset):
            thumbnail_path = UNSET
        else:
            thumbnail_path = self.thumbnail_path


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if change_note is not UNSET:
            field_dict["changeNote"] = change_note
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if object_key is not UNSET:
            field_dict["objectKey"] = object_key
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if thumbnail_path is not UNSET:
            field_dict["thumbnailPath"] = thumbnail_path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_change_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        change_note = _parse_change_note(d.pop("changeNote", UNSET))


        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))


        def _parse_object_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_key = _parse_object_key(d.pop("objectKey", UNSET))


        size_bytes = d.pop("sizeBytes", UNSET)

        def _parse_thumbnail_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_path = _parse_thumbnail_path(d.pop("thumbnailPath", UNSET))


        office_add_version_request = cls(
            change_note=change_note,
            content_type=content_type,
            object_key=object_key,
            size_bytes=size_bytes,
            thumbnail_path=thumbnail_path,
        )

        return office_add_version_request

