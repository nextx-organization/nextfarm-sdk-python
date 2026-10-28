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






T = TypeVar("T", bound="OfficeWikiPageVersionDto")



@_attrs_define
class OfficeWikiPageVersionDto:
    

    change_note: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    is_current: bool | Unset = UNSET
    title: None | str | Unset = UNSET
    version_number: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        change_note: None | str | Unset
        if isinstance(self.change_note, Unset):
            change_note = UNSET
        else:
            change_note = self.change_note

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_current = self.is_current

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        version_number = self.version_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if change_note is not UNSET:
            field_dict["changeNote"] = change_note
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if title is not UNSET:
            field_dict["title"] = title
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


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _created_by = d.pop("createdBy", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_current = d.pop("isCurrent", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        version_number = d.pop("versionNumber", UNSET)

        office_wiki_page_version_dto = cls(
            change_note=change_note,
            created_at=created_at,
            created_by=created_by,
            id=id,
            is_current=is_current,
            title=title,
            version_number=version_number,
        )

        return office_wiki_page_version_dto

