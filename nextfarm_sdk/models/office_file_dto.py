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






T = TypeVar("T", bound="OfficeFileDto")



@_attrs_define
class OfficeFileDto:
    

    content_type: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    current_version: int | Unset = UNSET
    folder_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    updated_by: None | Unset | UUID = UNSET
    version_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        current_version = self.current_version

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

        size_bytes = self.size_bytes

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        version_count = self.version_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if version_count is not UNSET:
            field_dict["versionCount"] = version_count

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




        current_version = d.pop("currentVersion", UNSET)

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


        size_bytes = d.pop("sizeBytes", UNSET)

        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)



                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))


        version_count = d.pop("versionCount", UNSET)

        office_file_dto = cls(
            content_type=content_type,
            created_at=created_at,
            created_by=created_by,
            current_version=current_version,
            folder_id=folder_id,
            id=id,
            name=name,
            size_bytes=size_bytes,
            thumbnail_url=thumbnail_url,
            updated_at=updated_at,
            updated_by=updated_by,
            version_count=version_count,
        )

        return office_file_dto

