from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeFileVersionDto")



@_attrs_define
class OfficeFileVersionDto:
    

    change_note: None | str | Unset = UNSET
    content_type: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_current: bool | Unset = UNSET
    size_bytes: int | Unset = UNSET
    uploaded_at: datetime.datetime | Unset = UNSET
    uploaded_by: UUID | Unset = UNSET
    version_number: int | Unset = UNSET





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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_current = self.is_current

        size_bytes = self.size_bytes

        uploaded_at: str | Unset = UNSET
        if not isinstance(self.uploaded_at, Unset):
            uploaded_at = self.uploaded_at.isoformat()

        uploaded_by: str | Unset = UNSET
        if not isinstance(self.uploaded_by, Unset):
            uploaded_by = str(self.uploaded_by)

        version_number = self.version_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if change_note is not UNSET:
            field_dict["changeNote"] = change_note
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if id is not UNSET:
            field_dict["id"] = id
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if uploaded_at is not UNSET:
            field_dict["uploadedAt"] = uploaded_at
        if uploaded_by is not UNSET:
            field_dict["uploadedBy"] = uploaded_by
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number

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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_current = d.pop("isCurrent", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        _uploaded_at = d.pop("uploadedAt", UNSET)
        uploaded_at: datetime.datetime | Unset
        if isinstance(_uploaded_at,  Unset):
            uploaded_at = UNSET
        else:
            uploaded_at = datetime.datetime.fromisoformat(_uploaded_at)




        _uploaded_by = d.pop("uploadedBy", UNSET)
        uploaded_by: UUID | Unset
        if isinstance(_uploaded_by,  Unset):
            uploaded_by = UNSET
        else:
            uploaded_by = UUID(_uploaded_by)




        version_number = d.pop("versionNumber", UNSET)

        office_file_version_dto = cls(
            change_note=change_note,
            content_type=content_type,
            id=id,
            is_current=is_current,
            size_bytes=size_bytes,
            uploaded_at=uploaded_at,
            uploaded_by=uploaded_by,
            version_number=version_number,
        )

        return office_file_version_dto

