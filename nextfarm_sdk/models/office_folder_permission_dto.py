from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_folder_permission_dto_permission_level import check_office_folder_permission_dto_permission_level
from ..models.office_folder_permission_dto_permission_level import OfficeFolderPermissionDtoPermissionLevel
from ..models.office_folder_permission_dto_principal_type import check_office_folder_permission_dto_principal_type
from ..models.office_folder_permission_dto_principal_type import OfficeFolderPermissionDtoPrincipalType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeFolderPermissionDto")



@_attrs_define
class OfficeFolderPermissionDto:
    

    folder_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    permission_level: OfficeFolderPermissionDtoPermissionLevel | Unset = UNSET
    principal_id: None | str | Unset = UNSET
    principal_type: OfficeFolderPermissionDtoPrincipalType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        folder_id: str | Unset = UNSET
        if not isinstance(self.folder_id, Unset):
            folder_id = str(self.folder_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        permission_level: str | Unset = UNSET
        if not isinstance(self.permission_level, Unset):
            permission_level = self.permission_level


        principal_id: None | str | Unset
        if isinstance(self.principal_id, Unset):
            principal_id = UNSET
        else:
            principal_id = self.principal_id

        principal_type: str | Unset = UNSET
        if not isinstance(self.principal_type, Unset):
            principal_type = self.principal_type



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if id is not UNSET:
            field_dict["id"] = id
        if permission_level is not UNSET:
            field_dict["permissionLevel"] = permission_level
        if principal_id is not UNSET:
            field_dict["principalId"] = principal_id
        if principal_type is not UNSET:
            field_dict["principalType"] = principal_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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




        _permission_level = d.pop("permissionLevel", UNSET)
        permission_level: OfficeFolderPermissionDtoPermissionLevel | Unset
        if isinstance(_permission_level,  Unset):
            permission_level = UNSET
        else:
            permission_level = check_office_folder_permission_dto_permission_level(_permission_level)




        def _parse_principal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_id = _parse_principal_id(d.pop("principalId", UNSET))


        _principal_type = d.pop("principalType", UNSET)
        principal_type: OfficeFolderPermissionDtoPrincipalType | Unset
        if isinstance(_principal_type,  Unset):
            principal_type = UNSET
        else:
            principal_type = check_office_folder_permission_dto_principal_type(_principal_type)




        office_folder_permission_dto = cls(
            folder_id=folder_id,
            id=id,
            permission_level=permission_level,
            principal_id=principal_id,
            principal_type=principal_type,
        )

        return office_folder_permission_dto

