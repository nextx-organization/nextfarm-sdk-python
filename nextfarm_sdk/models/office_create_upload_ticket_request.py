from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCreateUploadTicketRequest")



@_attrs_define
class OfficeCreateUploadTicketRequest:
    

    content_type: None | str | Unset = UNSET
    file_id: None | Unset | UUID = UNSET
    file_name: None | str | Unset = UNSET
    folder_id: UUID | Unset = UNSET
    size_bytes: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        elif isinstance(self.file_id, UUID):
            file_id = str(self.file_id)
        else:
            file_id = self.file_id

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        folder_id: str | Unset = UNSET
        if not isinstance(self.folder_id, Unset):
            folder_id = str(self.folder_id)

        size_bytes = self.size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes

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


        def _parse_file_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_id_type_0 = UUID(data)



                return file_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        file_id = _parse_file_id(d.pop("fileId", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        _folder_id = d.pop("folderId", UNSET)
        folder_id: UUID | Unset
        if isinstance(_folder_id,  Unset):
            folder_id = UNSET
        else:
            folder_id = UUID(_folder_id)




        size_bytes = d.pop("sizeBytes", UNSET)

        office_create_upload_ticket_request = cls(
            content_type=content_type,
            file_id=file_id,
            file_name=file_name,
            folder_id=folder_id,
            size_bytes=size_bytes,
        )

        return office_create_upload_ticket_request

