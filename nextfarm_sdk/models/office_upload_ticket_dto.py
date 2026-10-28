from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.office_upload_ticket_dto_fields_type_0 import OfficeUploadTicketDtoFieldsType0
  from ..models.office_upload_ticket_dto_headers_type_0 import OfficeUploadTicketDtoHeadersType0





T = TypeVar("T", bound="OfficeUploadTicketDto")



@_attrs_define
class OfficeUploadTicketDto:
    

    expires_at: datetime.datetime | Unset = UNSET
    fields: None | OfficeUploadTicketDtoFieldsType0 | Unset = UNSET
    headers: None | OfficeUploadTicketDtoHeadersType0 | Unset = UNSET
    method: None | str | Unset = UNSET
    object_key: None | str | Unset = UNSET
    thumbnail: OfficeUploadTicketDto | Unset = UNSET
    url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_upload_ticket_dto_fields_type_0 import OfficeUploadTicketDtoFieldsType0 # noqa: PLC0415
        from ..models.office_upload_ticket_dto_headers_type_0 import OfficeUploadTicketDtoHeadersType0 # noqa: PLC0415
        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        fields: dict[str, Any] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, OfficeUploadTicketDtoFieldsType0):
            fields = self.fields.to_dict()
        else:
            fields = self.fields

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, OfficeUploadTicketDtoHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        object_key: None | str | Unset
        if isinstance(self.object_key, Unset):
            object_key = UNSET
        else:
            object_key = self.object_key

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if fields is not UNSET:
            field_dict["fields"] = fields
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method
        if object_key is not UNSET:
            field_dict["objectKey"] = object_key
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_upload_ticket_dto_fields_type_0 import OfficeUploadTicketDtoFieldsType0 # noqa: PLC0415
        from ..models.office_upload_ticket_dto_headers_type_0 import OfficeUploadTicketDtoHeadersType0 # noqa: PLC0415
        d = dict(src_dict)
        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        def _parse_fields(data: object) -> None | OfficeUploadTicketDtoFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_type_0 = OfficeUploadTicketDtoFieldsType0.from_dict(data)



                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeUploadTicketDtoFieldsType0 | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))


        def _parse_headers(data: object) -> None | OfficeUploadTicketDtoHeadersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = OfficeUploadTicketDtoHeadersType0.from_dict(data)



                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeUploadTicketDtoHeadersType0 | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))


        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))


        def _parse_object_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_key = _parse_object_key(d.pop("objectKey", UNSET))


        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: OfficeUploadTicketDto | Unset
        if isinstance(_thumbnail,  Unset):
            thumbnail = UNSET
        else:
            thumbnail = OfficeUploadTicketDto.from_dict(_thumbnail)




        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        office_upload_ticket_dto = cls(
            expires_at=expires_at,
            fields=fields,
            headers=headers,
            method=method,
            object_key=object_key,
            thumbnail=thumbnail,
            url=url,
        )

        return office_upload_ticket_dto

