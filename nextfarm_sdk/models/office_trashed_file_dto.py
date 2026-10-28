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






T = TypeVar("T", bound="OfficeTrashedFileDto")



@_attrs_define
class OfficeTrashedFileDto:
    

    deleted_at: datetime.datetime | Unset = UNSET
    deleted_by: None | Unset | UUID = UNSET
    folder_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    purge_after: datetime.datetime | Unset = UNSET
    size_bytes: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        deleted_by: None | str | Unset
        if isinstance(self.deleted_by, Unset):
            deleted_by = UNSET
        elif isinstance(self.deleted_by, UUID):
            deleted_by = str(self.deleted_by)
        else:
            deleted_by = self.deleted_by

        folder_id: str | Unset = UNSET
        if not isinstance(self.folder_id, Unset):
            folder_id = str(self.folder_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        purge_after: str | Unset = UNSET
        if not isinstance(self.purge_after, Unset):
            purge_after = self.purge_after.isoformat()

        size_bytes = self.size_bytes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if purge_after is not UNSET:
            field_dict["purgeAfter"] = purge_after
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at,  Unset):
            deleted_at = UNSET
        else:
            deleted_at = datetime.datetime.fromisoformat(_deleted_at)




        def _parse_deleted_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_by_type_0 = UUID(data)



                return deleted_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deleted_by = _parse_deleted_by(d.pop("deletedBy", UNSET))


        _folder_id = d.pop("folderId", UNSET)
        folder_id: UUID | Unset
        if isinstance(_folder_id,  Unset):
            folder_id = UNSET
        else:
            folder_id = UUID(_folder_id)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _purge_after = d.pop("purgeAfter", UNSET)
        purge_after: datetime.datetime | Unset
        if isinstance(_purge_after,  Unset):
            purge_after = UNSET
        else:
            purge_after = datetime.datetime.fromisoformat(_purge_after)




        size_bytes = d.pop("sizeBytes", UNSET)

        office_trashed_file_dto = cls(
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            folder_id=folder_id,
            id=id,
            name=name,
            purge_after=purge_after,
            size_bytes=size_bytes,
        )

        return office_trashed_file_dto

