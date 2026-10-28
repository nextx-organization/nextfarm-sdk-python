from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeSendMessageAttachment")



@_attrs_define
class OfficeSendMessageAttachment:
    

    content_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    height: int | None | Unset = UNSET
    size_bytes: int | Unset = UNSET
    storage_path: None | str | Unset = UNSET
    thumbnail_path: None | str | Unset = UNSET
    width: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        size_bytes = self.size_bytes

        storage_path: None | str | Unset
        if isinstance(self.storage_path, Unset):
            storage_path = UNSET
        else:
            storage_path = self.storage_path

        thumbnail_path: None | str | Unset
        if isinstance(self.thumbnail_path, Unset):
            thumbnail_path = UNSET
        else:
            thumbnail_path = self.thumbnail_path

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if height is not UNSET:
            field_dict["height"] = height
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if storage_path is not UNSET:
            field_dict["storagePath"] = storage_path
        if thumbnail_path is not UNSET:
            field_dict["thumbnailPath"] = thumbnail_path
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))


        size_bytes = d.pop("sizeBytes", UNSET)

        def _parse_storage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_path = _parse_storage_path(d.pop("storagePath", UNSET))


        def _parse_thumbnail_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_path = _parse_thumbnail_path(d.pop("thumbnailPath", UNSET))


        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))


        office_send_message_attachment = cls(
            content_type=content_type,
            file_name=file_name,
            height=height,
            size_bytes=size_bytes,
            storage_path=storage_path,
            thumbnail_path=thumbnail_path,
            width=width,
        )

        return office_send_message_attachment

