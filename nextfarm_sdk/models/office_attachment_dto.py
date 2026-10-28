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






T = TypeVar("T", bound="OfficeAttachmentDto")



@_attrs_define
class OfficeAttachmentDto:
    

    content_type: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    entity_id: UUID | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    has_thumbnail: bool | Unset = UNSET
    height: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    size_bytes: int | Unset = UNSET
    storage_path: None | str | Unset = UNSET
    uploaded_by: UUID | Unset = UNSET
    version: int | Unset = UNSET
    width: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        has_thumbnail = self.has_thumbnail

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        size_bytes = self.size_bytes

        storage_path: None | str | Unset
        if isinstance(self.storage_path, Unset):
            storage_path = UNSET
        else:
            storage_path = self.storage_path

        uploaded_by: str | Unset = UNSET
        if not isinstance(self.uploaded_by, Unset):
            uploaded_by = str(self.uploaded_by)

        version = self.version

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if has_thumbnail is not UNSET:
            field_dict["hasThumbnail"] = has_thumbnail
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if storage_path is not UNSET:
            field_dict["storagePath"] = storage_path
        if uploaded_by is not UNSET:
            field_dict["uploadedBy"] = uploaded_by
        if version is not UNSET:
            field_dict["version"] = version
        if width is not UNSET:
            field_dict["width"] = width

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




        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entityType", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        has_thumbnail = d.pop("hasThumbnail", UNSET)

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        size_bytes = d.pop("sizeBytes", UNSET)

        def _parse_storage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_path = _parse_storage_path(d.pop("storagePath", UNSET))


        _uploaded_by = d.pop("uploadedBy", UNSET)
        uploaded_by: UUID | Unset
        if isinstance(_uploaded_by,  Unset):
            uploaded_by = UNSET
        else:
            uploaded_by = UUID(_uploaded_by)




        version = d.pop("version", UNSET)

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))


        office_attachment_dto = cls(
            content_type=content_type,
            created_at=created_at,
            entity_id=entity_id,
            entity_type=entity_type,
            file_name=file_name,
            has_thumbnail=has_thumbnail,
            height=height,
            id=id,
            size_bytes=size_bytes,
            storage_path=storage_path,
            uploaded_by=uploaded_by,
            version=version,
            width=width,
        )

        return office_attachment_dto

