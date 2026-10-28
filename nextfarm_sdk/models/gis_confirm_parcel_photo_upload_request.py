from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GisConfirmParcelPhotoUploadRequest")



@_attrs_define
class GisConfirmParcelPhotoUploadRequest:
    

    bucket: None | str | Unset = UNSET
    content_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    storage_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        bucket: None | str | Unset
        if isinstance(self.bucket, Unset):
            bucket = UNSET
        else:
            bucket = self.bucket

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

        size_bytes = self.size_bytes

        storage_key: None | str | Unset
        if isinstance(self.storage_key, Unset):
            storage_key = UNSET
        else:
            storage_key = self.storage_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if storage_key is not UNSET:
            field_dict["storage_key"] = storage_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_bucket(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bucket = _parse_bucket(d.pop("bucket", UNSET))


        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))


        size_bytes = d.pop("size_bytes", UNSET)

        def _parse_storage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_key = _parse_storage_key(d.pop("storage_key", UNSET))


        gis_confirm_parcel_photo_upload_request = cls(
            bucket=bucket,
            content_type=content_type,
            file_name=file_name,
            size_bytes=size_bytes,
            storage_key=storage_key,
        )

        return gis_confirm_parcel_photo_upload_request

