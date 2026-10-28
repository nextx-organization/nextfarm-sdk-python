from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerStickerUploadTicketRequest")



@_attrs_define
class OfficeChatControllerStickerUploadTicketRequest:
    

    content_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    size_bytes: int | Unset = UNSET





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

        size_bytes = self.size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
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


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        size_bytes = d.pop("sizeBytes", UNSET)

        office_chat_controller_sticker_upload_ticket_request = cls(
            content_type=content_type,
            file_name=file_name,
            size_bytes=size_bytes,
        )

        return office_chat_controller_sticker_upload_ticket_request

