from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_folder_dto_my_permission import check_office_folder_dto_my_permission
from ..models.office_folder_dto_my_permission import OfficeFolderDtoMyPermission
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeFolderDto")



@_attrs_define
class OfficeFolderDto:
    

    created_at: datetime.datetime | Unset = UNSET
    created_by: UUID | Unset = UNSET
    depth: int | Unset = UNSET
    file_count: int | Unset = UNSET
    id: UUID | Unset = UNSET
    is_restricted: bool | Unset = UNSET
    my_permission: OfficeFolderDtoMyPermission | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        depth = self.depth

        file_count = self.file_count

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_restricted = self.is_restricted

        my_permission: str | Unset = UNSET
        if not isinstance(self.my_permission, Unset):
            my_permission = self.my_permission


        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if depth is not UNSET:
            field_dict["depth"] = depth
        if file_count is not UNSET:
            field_dict["fileCount"] = file_count
        if id is not UNSET:
            field_dict["id"] = id
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if my_permission is not UNSET:
            field_dict["myPermission"] = my_permission
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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




        depth = d.pop("depth", UNSET)

        file_count = d.pop("fileCount", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_restricted = d.pop("isRestricted", UNSET)

        _my_permission = d.pop("myPermission", UNSET)
        my_permission: OfficeFolderDtoMyPermission | Unset
        if isinstance(_my_permission,  Unset):
            my_permission = UNSET
        else:
            my_permission = check_office_folder_dto_my_permission(_my_permission)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)



                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        office_folder_dto = cls(
            created_at=created_at,
            created_by=created_by,
            depth=depth,
            file_count=file_count,
            id=id,
            is_restricted=is_restricted,
            my_permission=my_permission,
            name=name,
            parent_id=parent_id,
        )

        return office_folder_dto

