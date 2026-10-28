from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatFolderDto")



@_attrs_define
class OfficeChatFolderDto:
    

    file_count: int | Unset = UNSET
    name: None | str | Unset = UNSET
    total_bytes: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        file_count = self.file_count

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        total_bytes = self.total_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if file_count is not UNSET:
            field_dict["fileCount"] = file_count
        if name is not UNSET:
            field_dict["name"] = name
        if total_bytes is not UNSET:
            field_dict["totalBytes"] = total_bytes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_count = d.pop("fileCount", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        total_bytes = d.pop("totalBytes", UNSET)

        office_chat_folder_dto = cls(
            file_count=file_count,
            name=name,
            total_bytes=total_bytes,
        )

        return office_chat_folder_dto

