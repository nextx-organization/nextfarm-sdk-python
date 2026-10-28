from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GisRequestPhotoUploadResult")



@_attrs_define
class GisRequestPhotoUploadResult:
    

    bucket: None | str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    max_bytes: int | Unset = UNSET
    storage_key: None | str | Unset = UNSET
    upload_url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        bucket: None | str | Unset
        if isinstance(self.bucket, Unset):
            bucket = UNSET
        else:
            bucket = self.bucket

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        max_bytes = self.max_bytes

        storage_key: None | str | Unset
        if isinstance(self.storage_key, Unset):
            storage_key = UNSET
        else:
            storage_key = self.storage_key

        upload_url: None | str | Unset
        if isinstance(self.upload_url, Unset):
            upload_url = UNSET
        else:
            upload_url = self.upload_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if max_bytes is not UNSET:
            field_dict["max_bytes"] = max_bytes
        if storage_key is not UNSET:
            field_dict["storage_key"] = storage_key
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url

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


        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        max_bytes = d.pop("max_bytes", UNSET)

        def _parse_storage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_key = _parse_storage_key(d.pop("storage_key", UNSET))


        def _parse_upload_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_url = _parse_upload_url(d.pop("upload_url", UNSET))


        gis_request_photo_upload_result = cls(
            bucket=bucket,
            expires_at=expires_at,
            max_bytes=max_bytes,
            storage_key=storage_key,
            upload_url=upload_url,
        )

        return gis_request_photo_upload_result

